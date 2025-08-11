---
description: |
  CeWL (Custom Word List generator) is a Ruby tool that spiders a given URL and generates a custom password wordlist based on the site’s content. This is useful for targeted password attacks, as it collects words that are likely relevant to the target organization (e.g., names, project titles, jargon).

  Command Reference:
  ```
  Depth (-d): 2

  Target URL: https://www.domein.nl/team

  Minimum Word Length: 3

  Only email addresses with -e

  Output File: words.txt
  ```
command: |
  cewl -d 2 -m 3 -w words.txt https://www.domein.nl/team 

items:
  - No_Creds
services:
  - Web
OS:
  - Linux
  - Mac
attack_types:
  - Enumeration
references:
  - https://github.com/digininja/CeWL
  - https://medium.com/@harshleenchawla06/discovering-the-basics-of-cewl-a5a57df1e604
---