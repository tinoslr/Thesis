#!/bin/bash
ping 192.168.0.1 -c 50 -i 0.2 > ping.txt

python3 readout.py