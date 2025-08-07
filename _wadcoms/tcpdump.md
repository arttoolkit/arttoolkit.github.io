---
description: |
  This command uses tcpdump to create a simple ICMP listener to test whether incoming ping (ICMP echo request) traffic is reaching my attacking machine. It's useful for basic network connectivity testing and for verifying whether firewalls or routing configurations are blocking ICMP traffic.

  Command Reference:
  ```
  Interface: tun0

  Filter: icmp and icmp[icmptype]=icmp-echo
  ```
command: |
  sudo tcpdump -i tun0 icmp and icmp[icmptype]=icmp-echo

items:
  - No_Creds
  - Shell
services:
  - General
OS:
  - Linux
  - Windows
  - Mac
attack_types:
  - General
references:
  - https://man7.org/linux/man-pages/man8/tcpdump.8.html
---