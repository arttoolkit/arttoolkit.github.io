---
description: |
  It is possible to assign special privileges to any user, independent of their group memberships. To do so, we can use the secedit command. Therefore, you have to convert the .inf file into a .sdb file which is then used to load the configuration back into the system. In the extra code is shown how to export the current config which you can modify, for example by adding users to privileges rights lines, and then convert it to .sdb and load back.

  Command Reference:
  ```
  config.sdb: database file holding the modified config

  config.inf: new configuration
  ```
command: |
  secedit /configure /db config.sdb /cfg config.inf

code: |
  secedit /export /cfg config.inf

  secedit /import /cfg config.inf /db config.sdb

  secedit /configure /db config.sdb /cfg config.inf

items:
  - Shell
  - Username
  - Password
OS:
  - Windows
attack_types:
  - Persistence
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/secedit
---