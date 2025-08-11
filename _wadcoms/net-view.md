---
description: |
  The net view command in Windows is used to display a list of shared resources on a remote machine. When combined with the /all flag, it provides additional details about hidden and administrative shares.

  Command Reference:
  ```
  Target Host: fs01

  Flags: /all (show all shares, including hidden ones)
  ```
command: |
  net view \\fs01 /all

code: |
  net view #Get a list of computers
  net view /all /domain [domainname] #Shares on the domains
  net view \\computer /ALL #List shares of a computer
  net share #Check current shares 

items:
  - ITEM
services:
  - SMB
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://book.hacktricks.wiki/en/windows-hardening/basic-cmd-for-pentesters.html#shares
  - https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh875576(v=ws.11)
---