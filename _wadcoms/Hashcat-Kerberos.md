---
description: |
  The command hashcat is a password recovery tool that allows for the cracking of various types of password hashes. The goal of the command is to attempt to crack the password hash (Kerberos) using a list of common passwords from the rockyou wordlist.

  Command Reference:
  ```
  Mode: 18200 (Kerberos 5 AS-REP etype 23)

  TGT hash: user.kerb

  Wordlist: /usr/share/wordlists/rockyou.txt
  ```
command: |
  hashcat -m 18200 user.kerb /usr/share/wordlists/rockyou.txt

code: |
  $krb5asrep$23$svc-alfresco@HTB:37a6233a6b2606aa39b55bff58654d5f$87335c1c890ae91dbd9a254a8ae27c06348f19754935f74473e7a41791ae703b95ed09580cc7b3ab80e1037ca98a52f7d6abd8732b2efbd7aae938badc90c5873af05eadf8d5d124a964adfb35d894c0e3b48$5f8a8b31f369d86225d3d53250c63b7220ce699efdda2c7d77598b6286b7ed1086dda0a19a21ef7881ba2b249a022adf9dc846785008408413e71ae008caf00fabbfa872c8657dc3ac82b4148563ca910ae72b8ac30bcea512fb94d78734f38ae7be1b73f8bae0bbfb49e6d61dc9d06d055004d29e7484cf0991953a4936c572df9d92e2ef86b5282877d07c38:s3rvice
 

items:
  - TGT
services:
  - Kerberos
OS:
  - Windows
attack_types:
  - Cracking
references:
  - https://hashcat.net/hashcat/
  - https://gist.github.com/TarlogicSecurity/2f221924fef8c14a1d8e29f3cb5c5c4a
  - https://infosecwriteups.com/hackthebox-forest-5a11553de1
---