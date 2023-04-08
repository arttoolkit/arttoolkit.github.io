---
description: |
  PSCredential is a PowerShell cmdlet used to create a credential object. It is used to securely store and retrieve usernames and passwords in scripts or commands. Via the GetNetworkCredential method it is possible to retrieve the password.  

  Command Reference:

  	Variable name: $cred

    Method: GetNetworkCredential

command: |
  $cred.GetNetworkCredential().Password

code: |
  $pass = ConvertTo-SecureString 'password123' -AsPlainText -Force

  $Cred = New-Object System.Management.Automation.PSCredential('htb.local\mmaas', $pass)

items:
  - Shell
services:
  - 
OS:
  - Windows
attack_types:
  - Cracking
references:
  - https://jatinpurohit.wordpress.com/2020/04/08/decrypt-pscredential-object-password-and-its-applications/
---
