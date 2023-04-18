---
description: |
  "CrackMapExec (a.k.a CME) is a post-exploitation tool that helps automate assessing the security of large Active Directory networks." - https://github.com/byt3bl33d3r/CrackMapExec/wiki. This command will enumerate the SMB host on domain users. 

  Command Reference:
  ```
  Target: flight.htb

  User: svc_apache

  Password: test1234
  ```

command: |
  crackmapexec smb flight.htb -u svc_apache -p 'test123' --users

co de: |
  This below command can be used to check for reused passwords, on other users in the users.txt

  crackmapexec smb flight.htb -u users.txt -p 'test123' --continue-on-success

items:
  - No_Creds
services:
  - SMB
attack_types:
  - Enumeration
  - Persistence
OS:
  - Linux
references:
  - https://github.com/byt3bl33d3r/CrackMapExec
  - https://github.com/byt3bl33d3r/CrackMapExec/wiki
---
