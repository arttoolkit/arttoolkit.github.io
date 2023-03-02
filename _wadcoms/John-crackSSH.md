---
description: |
  John the Ripper is a popular password cracking tool that uses a variety of techniques to guess passwords. When used to crack an SSH key, John can attempt to guess the passphrase used to encrypt the private key, allowing an attacker to gain unauthorized access to the remote server.

  Command Reference:
  ```
  Wordlist: /opt/wordlists/rockyou.txt

  Private SSH key in John format: sshkey.john
  ```
command: |
  john --wordlist=/opt/wordlists/rockyou.txt sshkey.john

code: |
  sshng2john.py id_rsa

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
  - https://github.com/openwall/john
  - https://null-byte.wonderhowto.com/how-to/crack-ssh-private-key-passwords-with-john-ripper-0302810/
  - https://github.com/Kyuu-Ji/htb-write-up/blob/master/tenten/write-up-tenten.md
---