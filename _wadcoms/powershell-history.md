---
description: |
  Whenever a user runs a command using Powershell, it gets stored into a file that keeps a memory of past commands. This is useful for repeating commands you have used before quickly. If a user runs a command that includes a password directly as part of the Powershell command line, it can later be retrieved by using the following command. Other useful files are also listed in the extra code section

  Command Reference:
  ```
  %userprofile%: only works in cmd, for powershell it must be $Env:userprofile
  ```
command: |
  type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt

code: |
  Other places with useful information:
    + C:\Unattend.xml
    + C:\Windows\Panther\Unattend.xml
    + C:\Windows\Panther\Unattend\Unattend.xml
    + C:\Windows\system32\sysprep.inf
    + C:\Windows\system32\sysprep\sysprep.xml 

items:
  - Shell
OS:
  - Windows
attack_types:
  - Enumeration
---