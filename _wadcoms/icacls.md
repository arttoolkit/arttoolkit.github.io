---
description: |
  icacls in Windows is a command-line tool for managing access control lists. From an attacker's viewpoint, exploiting icacls could lead to unauthorized modifications of file and directory permissions, potentially facilitating data exfiltration, privilege escalation, or network compromise. In this example is the basic command is shown to view the rights of file and in the extra code is shown how to give more permission. 

  Command Reference:
  ```
  c:\tasks\schtask.bat: file you want to see the rights.

  /grant: with the /grant parameter you can give additional rights to a file, for example to execute a file

  Everyone:F: gives everyone full (F) access
  ```
command: |
  icacls c:\tasks\schtask.bat

code: |
  icacls C:\Users\thm-unpriv\rev-svc3.exe /grant Everyone:F

  C:\> icacls c:\tasks\schtask.bat
  c:\tasks\schtask.bat NT AUTHORITY\SYSTEM:(I)(F)
                    BUILTIN\Administrators:(I)(F)
                    BUILTIN\Users:(I)(F)

items:
  - Shell
OS:
  - Windows
attack_types:
  - Enumeration
  - General
  - PrivEsc
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/icacls
---