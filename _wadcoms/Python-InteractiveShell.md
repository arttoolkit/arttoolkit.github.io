---
description: |
  Python command to make an interactive shell of your simple shell. The pty module let’s you spawn a psuedo-terminal that can fool commands like su into thinking they are being executed in a proper terminal.

  Command Reference:
  ```
  Variant of shell you will get: /bin/bash or /bin/sh
  ```
command: |
  python3 -c 'import pty;pty.spawn("/bin/bash")'

code: |
  python3 -c 'import pty;pty.spawn("/bin/bash")'

  ctrl + z

  stty raw -echo; fg 

items:
  - Shell
services:
  - 
OS:
  - Linux
  - Windows
attack_types:
  - Persistence
  - General
references:
  - https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/
---