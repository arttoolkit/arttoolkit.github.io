---
description: |
  This is useful for user account/password brute force guessing and username enumeration when usernames are based on the users' names. By attempting a few weak passwords across a large set of user accounts, user account lockout thresholds can be avoided.

  Command Reference:
  ```
  Firstname: maurits

  Lastname: maas
  ```
command: |
  ./username-anarchy maurits maas

items:
  - Password
  - Username
  - No_creds
services:
  -
OS:
  - Windows
  - Linux
attack_types:
  - Cracking
  - Enumeration
references:
  - https://github.com/urbanadventurer/username-anarchy
---