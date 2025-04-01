---
description: |
  sendEmail is a command-line utility used to send email messages through SMTP servers. It can be leveraged for phishing campaigns to send malicious links or attachments to targets. The following command sends a phishing email with a malicious link in both the subject and message body, encouraging the recipient to click a payload located at http://10.10.21.14/payload.hta.

  Command Reference:
  ```
  -s (SMTP server): 10.10.21.1

  -t (target): target@hacker.com

  -f (sender): sender@hacker.com

  Attacking IP address: 10.10.21.14 (hosting payload.hta)
  ```
command: |
  sendEmail -s 10.10.21.1 -t target@hacker.com -f sender@hacker.com -u "Click http://10.10.21.14/payload.hta" -m "click http://10.10.21.14/payload.hta"

items:
  - No_Creds
services:
  - SMTP
OS:
  - Windows
  - Mac
  - Linux
attack_types:
  - Exploitation
references:
  - https://github.com/mogaal/sendEmail
---