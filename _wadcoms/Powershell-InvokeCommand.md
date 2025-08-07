---
description: |
  This command demonstrates how to remotely execute a PowerShell command on another machine using the current user's context. It is issued from cmd.exe and launches PowerShell, which in turn uses Invoke-Command to run a command block on the remote host. This method relies on PowerShell Remoting and requires that the target host allows remote PowerShell execution (WinRM enabled) and that the current user has the necessary privileges on the remote system.

  Command Reference:
  ```
  Target Host: SRV01

  Executed Command: hostname
  ```
command: |
  powershell "invoke-command -ComputerName SRV01 -ScriptBlock {hostname}"
items:
  - Shell
services:
  - WMI
OS:
  - Windows
attack_types:
  - Exploitation
references:
  - https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.5
---