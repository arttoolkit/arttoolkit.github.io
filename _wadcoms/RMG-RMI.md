---
description: |
  Remote-Method-Guesser (RMG) is a Java RMI vulnerability scanner that is capable of identifying common RMI vulnerabilities automatically. 

  Command Reference:
  ```
  IP address: arttoolkit.hacker.com

  Port: 1099

  Function: enum

  ```
command: |
  java -jar rmg-4.4.1-jar-with-dependencies.jar enum 10.0.0.1 1099 
items:
  - No_Creds
Services:
  - RMI
OS:
  - Windows
  - Linux
  - Mac
attack_types:
  - Enumeration
  - Exploitation
references:
  - https://github.com/qtc-de/remote-method-guesser
---