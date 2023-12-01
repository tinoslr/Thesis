#!/bin/bash
#ping device in the network
#maybe use traceroute
# use parallel streams with increasing mbits 
ping 192.168.0.xxx -c 100 -i 0.2 > ping.txt

python3 readout.py