import re
import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt 
import matplotlib as mpl
mpl.style.use('ggplot')
import seaborn as sns
bandwith_list1=[]
bandwith_list2=[]
bandwith_list3=[]
maximum_bandwith=[50,60,70,75,80,85,90]
csa_list=[]

def extract_mbits_per_sec1(file_path1):
    
    with open(file_path1, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                # i dont know, google it. filters the bandwith part out of the ping.txt file
                match = re.search(r'(\d+\.\d+)\s(M|)bits/sec', line)
                if match:
                    # attach the value to the var = latency
                    bandwith = float(match.group(1))
                    # append latency to an list
                    bandwith_list1.append(bandwith)
            del bandwith_list1[-2:]
    return bandwith_list1

def extract_mbits_per_sec2(file_path2):
    
    with open(file_path2, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                # i dont know, google it. filters the bandwith part out of the ping.txt file
                match = re.search(r'(\d+\.\d+)\s(M|)bits/sec', line)
                if match:
                    # attach the value to the var = latency
                    bandwith = float(match.group(1))
                    # append latency to an list
                    bandwith_list2.append(bandwith)
            del bandwith_list2[-2:]
    return bandwith_list2

def extract_mbits_per_sec3(file_path3):
    
    with open(file_path3, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                # i dont know, google it. filters the bandwith part out of the ping.txt file
                match = re.search(r'(\d+\.\d+)\s(M|)bits/sec', line)
                if match:
                    # attach the value to the var = latency
                    bandwith = float(match.group(1))
                    # append latency to an list
                    bandwith_list3.append(bandwith)
            del bandwith_list3[-2:]
    return bandwith_list3

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


def pandas(bandwith_list1,bandwithlist_2,bandwithlist_3):
    s1 = pd.Series(bandwith_list1)
    s2 = pd.Series(bandwith_list2)
    s3 = pd.Series(bandwith_list3)
    fig, axes = plt.subplots(figsize=(10,7))
    

    s1.plot(kind='line')
    s2.plot(kind='line')
    s3.plot(kind='line')
    plt.ylabel('Throughput in Mbits')
    plt.xlabel('Time in seconds')
    plt.legend(['UE1','UE2','UE3'],loc="upper right")
    fig.savefig("../Pictures/Bandwith_iperf.pdf")
    fig.savefig("../Pictures/Bandwith_iperf.png")

    print(s1.describe())
    print(s2.describe())
    print(s3.describe())


def CSA_Plot(x_axis,y_axis):
    fig = plt.figure(figsize =(10, 7))
    plt.plot(x_axis,y_axis)
    plt.ylabel('CSA in %')
    plt.xlabel('Minimum Throughput in Mbits/s')
    plt.savefig("../Pictures/CSA_Throughput_Plot.png")

def BoxPlot_Troughput(data):
    fig = plt.figure(figsize =(10, 7))
    plt.boxplot(data)
    plt.savefig("../Pictures/CSA_Troughput_BoxPlot.png")


file_path1 = '../iperf1.txt'
file_path2 = '../iperf2.txt'
file_path3 = '../iperf3.txt'

extract_mbits_per_sec1(file_path1)
extract_mbits_per_sec2(file_path2)
extract_mbits_per_sec3(file_path3)
#calculate_bandwith_list(bandwith_list)
pandas(bandwith_list1,bandwith_list2,bandwith_list3)
#CSA_Plot(maximum_bandwith,csa_list)
#BoxPlot_Troughput(bandwith_list1)