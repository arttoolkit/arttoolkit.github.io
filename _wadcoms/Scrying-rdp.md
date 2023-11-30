---
description: |
  A new tool for collecting RDP, web and VNC screenshots all in one place

  Command Reference:
  ```
  Target: -t rdp://10.0.0.1
  ```
command: |
  ./scrying -t rdp://10.0.0.1
items:
  - No_creds
services:
  - RDP
  - Web
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://github.com/nccgroup/scrying
---