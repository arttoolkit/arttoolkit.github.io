---
description: |
  The "RunAs" function in PowerShell is used to run a specific command or script as a different user. This can be particularly useful when you need to execute commands or scripts with elevated privileges or within a different security context. When dealing with multiple domains, especially in an Active Directory environment, executing commands in a different domain requires careful consideration due to security boundaries. Which can be usefull to execute commands as a domain user on a non domain PC.

  Command Reference:
  ```
  Username: mmaas

  Domain: domain.local

  Command: powershell_ise.exe

  /netonly allows you to open a new process with alternative credentials
  ```
command: |
  runas /netonly /user:domain.local\mmaas powershell_ise.exe

items:
  - Shell
  - Username
  - Password
services:
  - 
OS:
  - Windows
attack_types:
  - Exploitation
  - Persistance
references:
  - https://counihan.co.za/blog/Using-RunAs-from-PowerShell/
---