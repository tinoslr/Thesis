import re

bandwith_list=[]

def extract_mbits_per_sec(file_path):

    # with open(file_path , 'r') as file:
    #     text = file.read()

    # mbits_sec_pattern =re.compile(r'(\d+\.\d+)\sMbits/sec')
    # matches = mbits_sec_pattern.findall(text)
    # print(matches)
    # bandwith_list.append(matches)


    with open(file_path, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                # i dont know, google it. filters the latency part out of the ping.txt file
                match = re.search(r'(\d+\.\d+)\sMbits/sec', line)
                if match:
                    # attach the value to the var = latency
                    bandwith = float(match.group(1))
                    # append latency to an list
                    bandwith_list.append(bandwith)  
    
    print(bandwith_list)
    return bandwith_list



def calculate_average(bandwith_list):
    sum = 0
    for i in bandwith_list:
        sum += i
    print (sum)

file_path= 'iperf.txt'
extract_mbits_per_sec(file_path)
calculate_average(bandwith_list)