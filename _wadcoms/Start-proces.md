---
description: |
  The Start-Process cmdlet in PowerShell is used to launch a new process (executable file) or open a document using the associated application. It provides a way to interact with the Windows operating system to initiate and control processes from within a PowerShell script or session. Which can be usefull to launch/execute processes as a domain user on a non domain PC.

  Command Reference:
  ```
  Username: mmaas

  Domain: domain.local

  Command: powershell_ise.exe

  -Credential: If you need to run the process with different credentials, you can provide a PSCredential object using this parameter. You can create a PSCredential object with the Get-Credential cmdlet.
  ```
command: |
  Start-Process 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell_ise.exe' -Credential 'domain.local\mmaas'
items:
  - Shell
  - Username
  - Password
OS:
  - Windows
attack_types:
  - Persistence
references:
  - https://counihan.co.za/blog/Using-RunAs-from-PowerShell/
---