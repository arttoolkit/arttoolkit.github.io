---
description: |
  To mount an SMB (Server Message Block) share using the mount command in Linux, you would typically use the cifs filesystem type, which is an implementation of the SMB protocol.

  Command Reference:
  ```
  Username: Guest

  password: empty

  Share: //10.129.253.46/Development

  Local folder: devel
  ```
command: |
  mount -t cifs -o vers=2.1,username='Guest',password='' //10.129.253.46/Development devel

items:
  - No_creds
  - Username
  - Password
services:
  - SMB
OS:
  - Linux
attack_types:
  - Enumeration
references:
  - https://www.chrisrmiller.com/mount-samba-share-in-ubuntu/
  - https://askubuntu.com/questions/1050460/how-to-mount-smb-share-on-ubuntu-18-04
---