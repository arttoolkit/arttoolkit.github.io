---
description: Command is used to convert some text in one encoding into another encoding. This can be used to copy a file from Linux to Windows.

  Command Reference:

  	File to copy: powershell.ps1

  	Encoding: UTF-16LE

command: |
  cat powershel.ps1 |iconv -t UTF-16LE |base64 -w 0

  powershell <base64> -enc
items:
  - Shell
services:
OS:
  - Windows
attack_types:
  - General
references:
  - LINK
  - LINK
---