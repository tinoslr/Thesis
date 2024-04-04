#!bin/bash

#Variables to declare
host_adress=10.101.166.6
bitrate=10M
port=5201
duration=20

number_of_devices=1
txt_file1=test1.txt



iperf3 -c $host_adress -t $duration -p $port -b $bitrate -R --logfile ../txtfiles/$txt_file1

python3 createplot.py "$txt_file1" "$number_of_devices"