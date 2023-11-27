import re
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

bandwith_list=[]
maximum_bandwith=[10,20,30,40,50]
csa_list=[]

def extract_mbits_per_sec(file_path):
    
    with open(file_path, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                # i dont know, google it. filters the bandwith part out of the ping.txt file
                match = re.search(r'(\d+\.\d+)\sMbits/sec', line)
                if match:
                    # attach the value to the var = latency
                    bandwith = float(match.group(1))
                    # append latency to an list
                    bandwith_list.append(bandwith)
            del bandwith_list[-2:]
    return bandwith_list

def calculate_bandwith_list(bandwith_list):
    counter = 0
    for j in maximum_bandwith:
        for i in bandwith_list:
             if i >= j:
                  counter +=1
        CSA = (counter*100)/ len(bandwith_list)
        csa_list.append(CSA)
        print('The CSA for a minimum Throughput of',j,'Mbits/s is:', CSA,'%')
        counter = 0
    return csa_list

def CSA_Plot(x_axis,y_axis):
    #plot figure and save it
    plt.plot(x_axis,y_axis)
    plt.ylabel('CSA in %')
    plt.xlabel('minimum Troughput in Mbits/s')
    plt.savefig("../Pictures/CSA_Throughput_Plot.png")


file_path = '../iperf.txt'
extract_mbits_per_sec(file_path)
calculate_bandwith_list(bandwith_list)
CSA_Plot(maximum_bandwith,csa_list)
