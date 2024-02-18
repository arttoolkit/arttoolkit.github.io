---
description: |
  This command shows the set of assigned privileges of the current user. However there are a couple of privileges that can be abused and those can be seen on the Priv2Admin GitHub.

command: |
  whoami /priv

items:
  - Shell
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://github.com/gtworek/Priv2Admin
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/whoami
---