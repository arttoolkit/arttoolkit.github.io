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
  positional arguments:
  {account,auth,ca,cert,find,forge,ptt,relay,req,shadow,template}
                        Action
    account             Manage user and machine accounts
    auth                Authenticate using certificates
    ca                  Manage CA and certificates
    cert                Manage certificates and private keys
    find                Enumerate AD CS
    forge               Create Golden Certificates
    ptt                 Inject TGT for SSPI authentication
    relay               NTLM Relay to AD CS HTTP Endpoints
    req                 Request certificates
    shadow              Abuse Shadow Credentials for account takeover
    template            Manage certificate templates 

items:
  - Username
  - Password
services:
  - LDAP
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://github.com/ly4k/Certipy
---