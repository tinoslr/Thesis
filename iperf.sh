#!bin/bash
iperf3 -c 192.168.0.171 -u  -b 75M > iperf.txt

python3 iperf.py