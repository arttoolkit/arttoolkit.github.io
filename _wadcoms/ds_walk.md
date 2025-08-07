---
description: |
  DS_Walk enumerates all possible files and directories on a web server where a .ds_store file can be publicly accessed and downloaded. The tool will traverse all directories until no further .ds_store files are found in subsequent directories.

  Command Reference:
  ```
  Port: 8080

  IP address or URL (-u): http://10.10.21.14:8080/
  ```
command: |
  python3 ds_walk.py -u http://10.10.21.14:8080/

items:
  - No_Creds
services:
  - Web
OS:
  - Mac
attack_types:
  - Enumeration
references:
  - https://github.com/Keramas/DS_Walk
---