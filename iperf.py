import re

bandwith_list=[]

def extract_mbits_per_sec(file_path):

    with open(file_path , 'r') as file:
        text = file.read()

    mbits_sec_pattern =re.compile(r'(\d+\.\d+)\sMbits/sec')
    matches = mbits_sec_pattern.findall(text)
    print(matches)
    bandwith_list.append(matches)

    # K= 2
    # bandwith_list = bandwith_list[: len(bandwith_list) - K]
    return bandwith_list

def calculate_average(bandwith_list):
    sum = 0
    for i in bandwith_list:
        sum += i
    print (sum)

file_path= 'iperf.txt'
extract_mbits_per_sec(file_path)
calculate_average(bandwith_list)