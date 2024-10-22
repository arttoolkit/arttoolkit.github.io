---
description: |
  Python command to set up a webserver on the port you specify.

  Command Reference:
  ```
  Port: 80

  -b: 127.0.0.1 you can bind a specific interface to host the webserver on
  ```
command: |
  python3 -m http.server 80

items:
  -
services:
  - Web
OS:
  - Windows
  - Mac
  - Linux
attack_types:
  - General
references:
  - https://realpython.com/python-http-server/
---