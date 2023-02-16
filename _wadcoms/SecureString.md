---
description: |
  ConvertTo-SecureString PowerShell command is used to convert plain text into an encrypted form that can be used for secure storage or transmission. It takes a plain text string and converts it to a secure string object that can be saved to a file or used in memory for authentication or encryption purposes.

  Command Reference:

  	Variable name: $pass

  	Password: password123

command: |
  $pass = ConvertTo-SecureString 'password123' -AsPlainText -Force
items:
  - Shell
services:

OS:
  - Windows
attack_types:
  - General
references:
  - https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/convertto-securestring?view=powershell-7.3
  - https://www.pdq.com/blog/secure-password-with-powershell-encrypting-credentials-part-1/
---
