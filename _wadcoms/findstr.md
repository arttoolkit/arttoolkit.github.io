---
description: |
  The findstr command in Windows searches for text strings within files. It can be used during post-exploitation or CTF challenges to locate flags, credentials, or other sensitive data hidden in files.

  Command Reference:
  ```
  Search String: "RASTA{"

  Search Path: C:\Users\tquinn\*.*

  /S – Search subdirectories recursively

  /M – Print only file names containing matches

  /C:"text" – Search for the exact string
  ```
command: |
  findstr /S /M /C:"RASTA{" C:\Users\tquinn\*.* 

items:
  - Shell
services:
  - 
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/findstr
---