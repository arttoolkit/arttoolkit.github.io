---
description: |
  In Windows, file and folder permissions are managed through Access Control Lists (ACLs). Using PowerShell, attackers with the necessary privileges can retrieve the current ACL of a file, create a new access rule, and grant full control to a chosen user or group. 

  Command Reference:
  ```
  Target File: C:\Users\Administrator\Desktop\flag.txt

  Granted To: Everyone

  Permission: FullControl / Modify / ReadAndExecute / Read / Write 
  ```
command: |
  Get-Acl "C:\Users\Administrator\Desktop\flag.txt"

code: |
  $acl = Get-Acl "C:\Users\Administrator\Desktop\flag.txt"
  $rule = New-Object System.Security.AccessControl.FileSystemAccessRule("Everyone", "FullControl", "Allow")
  $acl.SetAccessRule($rule)
  Set-Acl "C:\Users\Administrator\Desktop\flag.txt" $acl 

items:
  - Shell
services:
  - 
OS:
  - Windows
attack_types:
  - PrivEsc
references:
  - https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-acl?view=powershell-7.5
  - https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-acl?view=powershell-7.5
---