---
description: |
  Windows installer files (also known as .msi files) are used to install applications on the system. They usually run with the privilege level of the user that starts it. However, these can be configured to run with higher privileges from any user account (even unprivileged ones). This could potentially allow us to generate a malicious MSI file that would run with admin privileges.

  Command Reference:
  ```
  C:\Windows\Temp\malicious.msi: malicious msi containing, for example, reverse shell
  ```
command: |
  msiexec /quiet /qn /i C:\Windows\Temp\malicious.msi

code: |
  The below registers must be set in order to exploit this vulnerability:
  reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer
  reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer

items:
  - Shell
OS:
  - Windows
attack_types:
  - PrivEsc
references:
  - https://dmcxblue.gitbook.io/red-team-notes/privesc/unquoted-service-path
---