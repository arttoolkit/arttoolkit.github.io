---
description: |
  Certipy is an offensive tool for enumerating and abusing Active Directory Certificate Services (AD CS). The find command is useful for enumerating AD CS certificate templates, certificate authorities and other configurations.

  Command Reference:
  ```
  User: e.black

  Password: ypOSJXPqlDOxxbQSfEERy300

  IP address: 10.129.239.91
  ```
command: |
  certipy find -u e.black -p ypOSJXPqlDOxxbQSfEERy300 -dc-ip 10.129.239.91

code: |
    Check following properties in templates, makes them vulnerable for ESC1.

    Client Authentication               : True
    Enrollment Agent                    : True
    Any Purpose                         : True
    Enrollee Supplies Subject           : True
    Certificate Name Flag               : EnrolleeSuppliesSubject

items:
  - Username
  - Password
services:
  - ADCS
  - LDAP
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://github.com/ly4k/Certipy
---