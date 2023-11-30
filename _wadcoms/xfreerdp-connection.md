---
description: |
  xfreerdp is an X11 Remote Desktop Protocol (RDP) client which can be used to connect to servers which allow incoming RDP connection. Besides normal username/password login it support a Pass the Hass attack.

  Command Reference:
  ```
  Username: mmaas

  Password: password@1

  IP address: 10.0.0.1

  Hash: /pth:hash
  ```
command: |
  xfreerdp /u:'mmaas' /p:'password@1' /v:10.0.0.1
 
items:
  - Username
  - Password
  - Hash
services:
  - RDP
OS:
  - Windows
attack_types:
  - Persistence
references:
  - https://www.mankier.com/1/xfreerdp
  - https://kali.org/blog/passing-hash-remote-desktop/
---