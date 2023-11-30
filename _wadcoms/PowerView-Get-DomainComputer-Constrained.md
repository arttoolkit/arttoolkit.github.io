---
description: |
  Get-DomainComputer -TrustedToAuth is a PowerView PowerShell command used for Active Directory enumeration. It retrieves computer objects that are trusted for delegation to authenticate to other services, potentially revealing systems susceptible to credential abuse. This command assists in identifying computers with trusted relationships that might be exploited by attackers to gain unauthorized access, making it a crucial tool for assessing security risks in an Active Directory environment.

command: |
  Get-DomainComputer -Credential $Cred -TrustedToAuth

code: |
  $Cred = New-Object System.Management.Automation.PSCredential('htb.local\mmaas', $pass)

items:
  - Shell
services:
  - LDAP
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://powersploit.readthedocs.io/en/latest/Recon/Get-DomainComputer/
  - https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1
---
