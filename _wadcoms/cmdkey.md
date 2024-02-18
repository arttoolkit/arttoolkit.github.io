---
description: |
  Windows allows to use other users' credentials. This function also gives the option to save these credentials on the system. The command below will list saved credentials. While you can't see the actual passwords, if you notice any credentials worth trying, you can use them with the runas command and the /savecred option, as seen in extra code.

command: |
  cmdkey /list

code: |
  runas /savecred /user:admin cmd.exe 

items:
  - Shell
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmdkey
---