---
description: |
  A PowerShell module for exporting, importing, removing, permissioning, publishing Active Directory Certificate Templates. It also includes a DSC resource for creating AD CS templates using these functions. This was built with the intent of using DSC for rapid lab builds, but it could also be used in production environments to move templates between AD CS environments. This command is used for duplicating an excisting 

  Command Reference:
  ```
  Name of new created template: newMaus

  Name of duplicated template: "Subordinate Certification Authority"

  Identity: CODER.HTB\PKI Admins
  ```
command: |
  New-ADCSTemplate -DisplayName newMaus -JSON (Export-ADCSTemplate -DisplayName "Subordinate Certification Authority") -publish -Identity "CODER.HTB\PKI Admins"

code: |
  The ADCSTemplate module contains the following PowerShell functions:

    Export-ADCSTemplate
    Get-ADCSTemplate
    New-ADCSDrive
    New-ADCSTemplate
    Remove-ADCSTemplate
    Set-ADCSTemplateACL
 

items:
  - Shell
services:
  - LDAP
  - ADCS
OS:
  - Windows
attack_types:
  - Enumeration
  - Exploitation
references:
  - https://github.com/GoateePFE/ADCSTemplate
---