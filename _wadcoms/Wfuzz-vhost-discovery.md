---
description: |
  Wfuzz has been created to facilitate the task in web applications assessments and it is based on a simple concept: it replaces any reference to the FUZZ keyword by the value of a given payload.

  Command Reference:
  ```
  -u for target site: http://flight.htb/

  -w for wordlist: https

  Placeholder for vhosts (-H): FUZZ.flight.htb

  ```
command: |
  wfuzz -c -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt -u "http://flight.htb/" -H "Host: FUZZ.flight.htb" --hl 154


items:
  - No_creds
services:
  - Web
OS:
  - Windows
  - Linux
attack_types:
  - Enumeration
references:
  - https://github.com/xmendez/wfuzz
  - https://wfuzz.readthedocs.io/en/latest/
---