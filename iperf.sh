#!bin/bash
iperf3 -c 192.168.0.131 -u -R -b 1000M > iperf.txt

python3 iperf.py