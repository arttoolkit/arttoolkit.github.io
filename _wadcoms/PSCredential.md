---
description: |
  PSCredential is a PowerShell cmdlet used to create a credential object. It is used to securely store and retrieve usernames and passwords in scripts or commands. The PSCredential cmdlet requires a username and a SecureString object for the password. 

  Command Reference:

  	Variable name: $Cred

    Username: htb.local\mmaas

  	Password: $pass = ConvertTo-SecureString 'password123' -AsPlainText -Force

command: |
  $Cred = New-Object System.Management.Automation.PSCredential('htb.local\mmaas', $pass)
items:
  - Shell
services:

OS:
  - Windows
attack_types:
  - General
references:
  - https://learn.microsoft.com/en-us/powershell/scripting/learn/deep-dives/add-credentials-to-powershell-functions?view=powershell-7.3
  - https://pscustomobject.github.io/powershell/howto/PowerShell-Create-Credential-Object/
---
