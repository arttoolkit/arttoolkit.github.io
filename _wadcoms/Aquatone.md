---
description: |
  Aquatone is a tool for visual inspection of websites across a large amount of hosts and is convenient for quickly gaining an overview of HTTP-based attack surface.

  Command Reference:
  ```
  List with IP address to enumerate: all-ips.txt

  Ports, if you want uncommon: -ports "10080,1080,2030,2443,9025,9090,9800,9801"

  Location of Chromium: C:\Users\test1\AppData\Local\Chromium\Application\chrome.exe
  ```
command: |
  cat .\all-ips.txt | .\aquatone.exe -chrome-path C:\Users\test1\AppData\Local\Chromium\Application\chrome.exe -out all-ip

code: |
  To avoid errors with making screenshots on Windows, make sure to put the Aquatone executable in the same folder as the Chromium executable. 
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
  - https://github.com/michenriksen/aquatone
---