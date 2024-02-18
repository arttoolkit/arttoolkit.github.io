---
description: |
  "wmic useraccounts" is a Windows Management Instrumentation Command-line utility that retrieves information about user accounts on a system, providing details such as username, full name, and SID. This example gives the username with corresponding SID.

command: |
  wmic useraccount get name,sid

items:
  - Shell
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://www.lifewire.com/how-to-find-a-users-security-identifier-sid-in-windows-2625149
---