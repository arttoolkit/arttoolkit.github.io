---
description: |
  Get-SQLInstanceDomain is a function in PowerUpSQL, a PowerShell module for SQL Server exploitation. It enumerates SQL Server instances within the current domain, aiding in identifying database servers. This command assists security professionals in assessing database security by locating instances that might be susceptible to unauthorized access or attacks. This command can be executed from a non-domain joined device if you have credentials, but on a domain joined machine you do not need to specify the credentials.

  Command Reference:
  ```
  IP address Domaincontroller: 10.0.0.1

  Domain: domain.local

  User: mmaas

  Password: Password123
  ```
command: |
  Get-SQLInstanceDomain -Verbose -DomainController 10.0.0.1 -Username domain.local\mmaas -password Password123
items:
  - Shell
services:
  - SQL
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://github.com/NetSPI/PowerUpSQL/wiki/PowerUpSQL-Cheat-Sheet
  - https://github.com/NetSPI/PowerUpSQL/blob/master/PowerUpSQL.ps1
---