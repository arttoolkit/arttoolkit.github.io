---
description: |
  sshng2john is a tool used to convert SSH private keys in OpenSSH format to a format that can be cracked using password cracking tools like John the Ripper. This can finally result in cracking the password of the private key.

  Command Reference:
  ```
  Private SSH key: id_rsa
  ```
command: |
  python3 ssh2john.py id_rsa.enc > sshkey.john

code: |
  john --wordlist=/opt/wordlists/rockyou.txt sshkey.john

items:
  - SSH_key
services:
  - SSH
OS:
  - Windows
  - Linux
attack_types:
  - Cracking
references:
  - https://github.com/openwall/john/blob/bleeding-jumbo/run/ssh2john.py
  - https://github.com/Kyuu-Ji/htb-write-up/blob/master/tenten/write-up-tenten.md
---