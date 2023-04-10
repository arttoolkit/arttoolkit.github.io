---
description: |
  netstat is a command-line network tool that is a handy for enumerating services that are running on a machine. This command shows all the active network services using the TCP protocol.

  Command Reference:
  ```
  protocol: tcp ( udp, icmp, ip, tcpv6, udpv6, icmpv6, or ipv6.)

  -a: Displays all active TCP connections and the TCP and UDP ports on which the computer is listening.

  -o: Displays active TCP connections and includes the process ID (PID) for each connection.

  -n: Displays active TCP connections, however, addresses and port numbers are expressed numerically and no attempt is made to determine names.
  ```
command: |
  netstat -aon -p tcp

items:
  - Shell
services:
  - 
OS:
  - Windows
attack_types:
  - Enumeration
references:
  - https://geekflare.com/netstat-command-usage-on-windows/
  - LINK
---