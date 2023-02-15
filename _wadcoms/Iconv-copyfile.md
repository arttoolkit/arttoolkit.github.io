---
description: |
    Iconv s a command-line program used to convert text from one character encoding to another. It can be used to convert text files from one encoding to another, or to perform character set conversions when moving text between different operating systems or applications. It is useful for copying files from Linux to Windows as it can encode powershell files and execute it on the Windows machine.

    Command Reference:

        Copy file from Linux to Windows

        File to copy: powershell.ps1
        
        encoding: UTF-16LE

        Windows command: powershell <base64> -enc

command: |
  cat powershel.ps1 |iconv -t UTF-16LE |base64 -w 0

items:
  - Shell
services:
OS:
  - Windows
attack_types:
  - General
references:
  - https://www.gnu.org/savannah-checkouts/gnu/libiconv/documentation/libiconv-1.17/iconv.1.html#SEC7
---