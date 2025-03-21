---
description: |
  Impacket-secretsdump can extract credential information from a target machine. Instead of connecting to a live system, this command extracts NTLM hashes, LSA secrets, and other credentials from offline SYSTEM and SAM registry hive files. This is useful when access to a machine is already obtained, and the registry hives are dumped for offline analysis.

  Command Reference:

  	-system: system.hive of target machine

  	-sam: sam.hive of target machine

command: |
  impacket-secretsdump -system system.hive -sam sam.hive LOCAL
items:
  - Shell
services:
  - Kerberos
  - NTLM
OS:
  - Linux
  - Windows
attack_types:
  - Exploitation
references:
  - https://github.com/SecureAuthCorp/impacket/blob/master/examples/secretsdump.py
  - https://www.thehacker.recipes/ad/movement/credentials/dumping/sam-and-lsa-secrets
---
