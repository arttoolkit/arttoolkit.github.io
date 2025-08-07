---
description: |
  The takeown command is used in Windows to take ownership of files or directories, which can allow a user to access or manipulate files they otherwise wouldn’t have permission to. This is especially useful during post-exploitation when the user has local administrator privileges but lacks access to specific files (e.g. protected documents, loot, or flags).

  Command Reference:
  ```
  Target File: C:\Users\Username\Desktop\flag.txt

  /f: Specifies the file name or directory name pattern. You can use the wildcard character * when specifying the pattern. You can also use the syntax <sharename>\<filename>.
  ```
command: |
  takeown /f "C:\Users\Username\Desktop\flag.txt"

code: |
  icacls "C:\Users\Username\Desktop\flag.txt" /grant Administrators:F 

items:
  - Shell
services:
  - 
OS:
  - Windows
attack_types:
  - PrivEsc
  - Exploitation
  - Gerneal
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/takeown
---