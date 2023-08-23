---
description: |
  The Get-SQLInstanceDomain identifies all the SQL servers in the domain. This in combination with the Get-SQLConnectionTestThreaded tests whether the credentials supplied allow access to these servers. With this command an attacker can enumerate to which server it has access with found or guessed credentials. This command can be executed from a non-domain joined device, however you need to have reachability to the DomainController

  Command Reference:
  ```
  IP address Domaincontroller: 10.0.0.1

  Domain: domain.local

  User: mmaas

  Password: Password123
  ```
command: |
  Get-SQLInstanceDomain -Verbose -DomainController 10.0.0.1 -Username domain.local\mmaas -password Password123| Get-SQLConnectionTestThreaded -Verbose -Threads 3 | Where-Object {$_.Status -like "Accessible"}
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