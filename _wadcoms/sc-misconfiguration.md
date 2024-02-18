---
description: |
  Each service on a Windows machine will have an associated executable which will be run by the Service Control Manager (SCM) whenever a service is started. The associated executable is specified through the BINARY_PATH_NAME parameter, and the account used to run the service is shown on the SERVICE_START_NAME parameter. Of you have permission on the BINARY_PATH_NAME you can evelvate your rights to the user as mention in SERVICE_START_NAME. 
  
  Another point of interest is the unquoted BINARY_PATH_NAME, as in the extra code, Windows interpretation will be "C:\MyPrograms\Disk.exe". So if you have control over the directory you can create a malicious executable.

  Command Reference:
  ```
  "disk sorter enterprise": Service on the Windows machine
  ```
command: |
  sc qc "disk sorter enterprise"

code: |
  List all services on machine:
  sc queryex type= service state= all OR via TaskManager

  C:\> sc qc "disk sorter enterprise"
  [SC] QueryServiceConfig SUCCESS

  SERVICE_NAME: disk sorter enterprise
          TYPE               : 10  WIN32_OWN_PROCESS
          START_TYPE         : 2   AUTO_START
          ERROR_CONTROL      : 0   IGNORE
          BINARY_PATH_NAME   : C:\MyPrograms\Disk Sorter Enterprise\bin\disksrs.exe
          LOAD_ORDER_GROUP   :
          TAG                : 0
          DISPLAY_NAME       : Disk Sorter Enterprise
          DEPENDENCIES       :
          SERVICE_START_NAME : .\svcusr2 
  
  Oneliner for locating unquoted service paths:
  wmic service get name,displayname,startmode,pathname | findstr /i /v "C:\Windows\\" |findstr /i /v """

items:
  - Shell
OS:
  - Windows
attack_types:
  - Enumeration
  - PrivEsc
references:
  - https://www.ired.team/offensive-security/privilege-escalation/unquoted-service-paths
---