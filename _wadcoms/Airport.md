---
description: |
  "Airport" in macOS, accessed via the "System Information" app or Terminal with options like -s and -I, provides in-depth WiFi statistics with a security focus. The -s flag lists WiFi networks with security information like encryption type, while -I delivers comprehensive details about a specific network, aiding users and administrators in assessing the security posture of wireless connections. This feature empowers users to make informed decisions and take measures to enhance the security of their WiFi interactions on Mac devices.

  Command Reference:
  ```
  -s: Perform a wireless broadcast scan.

  -I: Print current wireless status, e.g. link auth, signal info, BSSID, port type etc.
  ```
command: |
  /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s

code: |
  /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I

items:
  - Shell
OS:
  - Mac
attack_types:
  - Enumeration
  - General
references:
  - https://ss64.com/osx/airport.html
---