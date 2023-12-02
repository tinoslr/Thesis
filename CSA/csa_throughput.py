import re
import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt 
import matplotlib as mpl
mpl.style.use('ggplot')
import seaborn as sns
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


def pandas(bandwith_list):
    s = pd.Series(bandwith_list)
    fig, axes = plt.subplots(figsize=(10,7))

    s.plot(kind='line')
    plt.ylabel('Bandwith in Mbits')
    plt.xlabel('Data Packets')
    fig.savefig("../Pictures/Bandwith_ping.pdf")
    fig.savefig("../Pictures/Bandwith_ping.png")

    print(s.describe())


def CSA_Plot(x_axis,y_axis):
    fig = plt.figure(figsize =(10, 7))
    plt.plot(x_axis,y_axis)
    plt.ylabel('CSA in %')
    plt.xlabel('minimum Troughput in Mbits/s')
    plt.savefig("../Pictures/CSA_Throughput_Plot.png")

def BoxPlot_Troughput(data):
    fig = plt.figure(figsize =(10, 7))
    plt.boxplot(data)
    plt.savefig("../Pictures/CSA_Troughput_BoxPlot.png")


file_path = '../iperf.txt'
extract_mbits_per_sec(file_path)
calculate_bandwith_list(bandwith_list)
pandas(bandwith_list)
CSA_Plot(maximum_bandwith,csa_list)
BoxPlot_Troughput(bandwith_list)