---
description: |
  Evil-WinRM uses the Windows Management Instrumentation (WMI) to give you an interactive shell on the Windows host.

  Command Reference:

  	Target IP: 10.10.10.1

  	Username: john

  	Password: password123

  	Hash (-H):  807726fcf9f188adc26eeafd7dc16bb7

command: |
  evil-winrm -i 10.10.10.1 -u john -p password123
items:
  - Password
  - Username
  - Hash
services:
  - WMI
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
  - Persistence
references:
  - https://github.com/Hackplayers/evil-winrm
---
