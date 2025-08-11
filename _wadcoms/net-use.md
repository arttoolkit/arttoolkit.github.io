---
description: |
  The net use command in Windows is used to connect to shared resources, such as shared folders or printers. It can also be used to map a network drive to a specific drive letter and authenticate with supplied credentials (or with current shell context when not providing creds). 

  Command Reference:
  ```
  Remote share: \\fs01.hacker.com\home$\mmaas

  Username: mmaas

  Drive Letter: H: (to which you mount)
  ```
command: |
  net use H: \\fs01.hacker.com\home$\mmaas /user:mmaas "PASS"

code: |
  net use x: \\fs01.hacker.com\home$\mmaas

items:
  - Shell
  - Username
  - Password
services:
  - SMB
OS:
  - Windows
attack_types:
  - Exploitation
references:
  - https://book.hacktricks.wiki/en/windows-hardening/basic-cmd-for-pentesters.html#shares
  - https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/gg651155(v=ws.11)
---