---
description: |
  This command mounts a shared folder from the host system into a VMware virtual machine using vmhgfs-fuse. It allows the VM to access files stored on the host. This is especially useful for transferring scripts, payloads, or loot between the host and the guest VM during an engagement. The command mounts the root of the shared folders (.host:/) to the local mount point /mnt/ and sets permissions so that all users in the VM can access it.

  Command Reference:
  ```
  Mount Source: .host:/ (VMware shared folders)

  Mount Target: /mnt/

  Options: allow_other (allow all users to access the mount)
  ```
command: |
  sudo vmhgfs-fuse .host:/ /mnt/ -o allow_other
items:
  - No_creds
  - Shell
services:
  - 
OS:
  - Linux
attack_types:
  - General
references:
  - https://infosam.medium.com/sharing-a-folder-to-a-kali-linux-vm-in-vmware-fusion-c24450e14895
---