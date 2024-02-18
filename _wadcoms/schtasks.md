---
description: |
  Scheduled tasks can be listed from the command line using the 'schtasks' command without any options. To retrieve detailed information about any of the specific tasks, you can use the below command. Within the output of this command Task to Run and Run as User are specified, if you have access (modify/write) to the executable it is possible to perform action with the privilege of Run As User.

  Command Reference:
  ```
  vuln_task: tasks which is found.

  Task to Run: Executable which is used in the tasks

  Run as User: User in which context the tasks runs (so you can elavate to this user)
  ```
command: |
  schtasks /query /tn vuln_task /fo list /v

code: |
  C:\> schtasks /query /tn vulntask /fo list /v
  Folder: \
  HostName:                             THM-PC1
  TaskName:                             \vulntask
  Task To Run:                          C:\tasks\schtask.bat
  Run As User:                          taskusr1 

items:
  - Shell
OS:
  - Windows
attack_types:
  - Enumeration
  - PrivEsc
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks
---