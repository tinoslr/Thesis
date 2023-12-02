#!/bin/bash
#ping device in the network
#maybe use traceroute
# use parallel streams with increasing mbits 
ping 192.168.178.163 -c 1000 -i 0.2 > ping.txt

python3 readout.py