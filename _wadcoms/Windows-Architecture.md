---
description: |
  Identifying the Windows architecture (32-bit or 64-bit) is crucial during an attack to ensure the correct payloads and exploits are used. The following commands retrieve the operating system architecture using both Command Prompt (WMIC) and PowerShell.

command: |
  wmic os get OSArchitecture

code: |
  [System.Environment]::Is64BitOperatingSystem 

items:
  - Shell
services:
  - General
OS:
  - Windows
attack_types:
  - Enumeration
references:

---