#!bin/bash

iperf3 -s -D --logfile M5a.txt -p 5001
iperf3 -s -D --logfile M5b.txt -p 5002
iperf3 -s -D --logfile M5c.txt -p 5003
iperf3 -s -D --logfile M5d.txt -p 5004
iperf3 -s -D --logfile M5e.txt -p 5005