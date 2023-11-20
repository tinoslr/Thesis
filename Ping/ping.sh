#!/bin/bash
ping www.google.com -c 100 -i 0.2 > ping.txt

python3 readout.py