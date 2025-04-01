---
description: |
  Swaks (Swiss Army Knife for SMTP) is a powerful command-line tool that allows for testing and sending emails. It can be leveraged for phishing campaigns to send malicious attachments to unsuspecting users. The following command sends an email with the subject "READ", body text "Please see attached", and attaches a malicious document (test.docm). The email is sent using the SMTP server at 10.10.21.1.

  Command Reference:
  ```
  -s (SMTP server): 10.10.21.1

  -t (target): target@hacker.com

  -f (sender): sender@hacker.com

  --attach: file to send as attachment
  ```
command: |
  swaks --header "Subject: READ" --body 'Please see attached' -t target@hacker.com -f sender@hacker.com --server 10.10.21.14 --attach @test.docm

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