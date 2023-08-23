---
description: |
  From an attacker's perspective, PingCastle is a powerful Active Directory security tool. It assists in identifying vulnerabilities, misconfigurations, and potential attack vectors within Active Directory environments. With detailed reports, it exposes weaknesses like privilege escalation paths, outdated systems, and permissions vulnerabilities. Utilizing PingCastle, attackers can gain insights to plan targeted attacks, escalate privileges, and exploit weaknesses in compromised Active Directory infrastructures. In this example we use credentials to retrieve information but it can be used to extract extra information.
  
  Command Reference:
  ```
  Domain: arttoolkit.hacker.com

  --user: user in the domain

  --password: password of the user

  --server: IP address of domain controller or domain name
  ```
command: |
  PingCastle.exe --healthcheck --user mmaas --password [pass] --server [ip] 

code: |
  PingCastle.exe --healthcheck --server mydomain.com

items:
  - Shell
services:
  - LDAP
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://www.pingcastle.com/documentation/healthcheck/
  - https://github.com/vletoux/pingcastle
---