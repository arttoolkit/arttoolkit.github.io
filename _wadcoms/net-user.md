---
description: |
  The net user command can be used in Windows to query details about a specific user, which can be locally or within the Active Directory domain. This can reveal information such as group memberships, last logon, password policies, and account status.

  Command Reference:
  ```
  Target User: mmaas

  Domain Flag: /domain (queries the domain)
  ```
command: |
  net user mmaas /domain

items:
  - Shell
services:
  - LDAP
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://book.hacktricks.wiki/en/windows-hardening/basic-cmd-for-pentesters.html#users
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/net-user
---