---
description: |
  Get-DomainComputer -Unconstrained is a PowerShell command provided by the PowerView module for Active Directory enumeration. It retrieves computer objects within a domain that have unconstrained delegation enabled, potentially indicating security vulnerabilities. This command helps identify systems that might allow attackers to impersonate users or escalate privileges through unconstrained delegation, which should be investigated and secured promptly. It's a valuable tool for auditing Active Directory environments for potential security risks. 

command: |
  Get-DomainComputer -Credential $Cred -Unconstrained

code: |
  $Cred = New-Object System.Management.Automation.PSCredential('htb.local\mmaas', $pass)

items:
  - Shell
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://powersploit.readthedocs.io/en/latest/Recon/Get-DomainComputer/
---
