#!/bin/bash

# Gib hier den gewünschten Pfad an, wo die Logdateien gespeichert werden sollen
log_path="/home/tino/Thesis"

iperf3 -s --logfile "${log_path}M4a.txt" -p 5001
iperf3 -s --logfile "${log_path}M4b.txt" -p 5002
iperf3 -s --logfile "${log_path}M4c.txt" -p 5003
iperf3 -s --logfile "${log_path}M4d.txt" -p 5004