---
description: |
  This command list the software that is available on the Windows machine. It can be useful to enumerate the software versions and check for known vulnerabilities and public exploit. Use exploit-db.

command: |
  wmic product get name,version,vendor

items:
  - Shell
OS:
  - Windows
attack_types:
  - Enumeration
  - General
references:
  - https://www.exploit-db.com/
---