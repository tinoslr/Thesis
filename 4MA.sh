#!bin/bash

iperf3 -s -D --logfile M4a.txt -p 5001
iperf3 -s -D --logfile M4b.txt -p 5002
iperf3 -s -D --logfile M4c.txt -p 5003
iperf3 -s -D --logfile M4d.txt -p 5004
