---
description: |
  The xattr command can be used to display, modify or remove the extended attributes (like quarantine) of one or more files, including directories and symbolic links. Extended attributes are arbitrary metadata stored with a file, but separate from the filesystem attributes (such as modification time or file size).

  Command Reference:
  ```
  Attribute: com.apple.quarantine (Quarantine)

  Application in quarantine: Bloodhoud.app
  ```
command: |
  xattr -d com.apple.quarantine Bloodhound.app
 
items:
  - Shell
services:
  - AV
OS:
  - Mac
attack_types:
  - Bypassing
references:
  - https://keith.github.io/xcode-man-pages/xattr.1.html
  - https://derflounder.wordpress.com/2012/11/20/clearing-the-quarantine-extended-attribute-from-downloaded-applications/
---