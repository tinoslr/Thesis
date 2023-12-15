import re
import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt 
import matplotlib as mpl
mpl.style.use('ggplot')
import seaborn as sns
from scipy.stats import gaussian_kde


bandwith_list1=[]
bandwith_list2=[]
bandwith_list3=[]



def extract_mbits_per_sec1(file_path1):
    #This function extracts the Throughput of an iperf1.txt file
    
    with open(file_path1, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                # i dont know, google it. filters the bandwith part out of the ping.txt file
                match = re.search(r'(\d+(\.\d+)?)\s(M|)bits/sec', line)
                if match:
                    # attach the value to the var = latency
                    bandwith = float(match.group(1))
                    if bandwith > 650:
                    # append throughput to an list
                        bandwith_list1.append(bandwith)
                    

            del bandwith_list1[-2:]
    return bandwith_list1

def extract_mbits_per_sec2(file_path2):
    #This function extracts the Throughput of an iperf2.txt file

    with open(file_path2, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                # i dont know, google it. filters the bandwith part out of the ping.txt file
                match = re.search(r'(\d+(\.\d+)?)\s(M|)bits/sec', line)
                if match:
                    # attach the value to the var = latency
                    bandwith = float(match.group(1))
                    if bandwith > 45:
                    # append latency to an list
                        bandwith_list2.append(bandwith)
            del bandwith_list2[-2:]
    return bandwith_list2

def extract_mbits_per_sec3(file_path3):
    #This function extracts the Throughput of an iperf3.txt file
    
    with open(file_path3, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                # i dont know, google it. filters the bandwith part out of the ping.txt file
                match = re.search(r'(\d+(\.\d+)?)\s(M|)bits/sec', line)
                if match:
                    # attach the value to the var = latency
                    bandwith = float(match.group(1))
                    # append latency to an list
                    if bandwith > 45:
                        bandwith_list3.append(bandwith)
            del bandwith_list3[-2:]
    return bandwith_list3

def extract_troughput(filepaths,all_lists):
    try:
        for filepath, current_list in zip(filepaths,all_lists):
            with open(filepath, 'r') as file:
                    lines = file.readlines()
                    for i, line in enumerate(lines, start=1):
                        # i dont know, google it. filters the bandwith part out of the ping.txt file
                        match = re.search(r'(\d+(\.\d+)?)\s(M|)bits/sec', line)
                        if match:
                            # attach the value to the var = latency
                            bandwith = float(match.group(1))
                            if bandwith > 60:
                            # append throughput to an list
                                current_list.append(bandwith)
                        
    
                    del current_list[-2:]
    except FileNotFoundError:
        print(f"Die Datei '{filepath}' wurde nicht gefunden.")                
    return 

def pandas(bandwith_list1):
    s1 = pd.Series(bandwith_list1)

   #create a plot with 2 subplots 
    fig, axes = plt.subplots(1, 2,figsize=(10,6))

    # configuration of plot 1 
    s1.plot(ax=axes[0],kind='line')
    axes[0].set_xlabel('Time in s')
    axes[0].set_ylabel('Throughput in Mbit/s')
    

    #configuration of plot 2
    s1.plot(ax=axes[1],kind='kde')
    axes[1].set_xlabel('Throughput in Mbit/s')
    axes[1].set_ylabel('Density')
    plt.xlim(120, 250)
    plt.legend(['UE1'],loc="upper right")

    # make it fit better
    plt.tight_layout()
    fig.savefig("../Pictures/Bandwith_iperf.pdf")
    
    print(s1.describe())

def pandas2(bandwith_list1,bandwith_list2):
    s1 = pd.Series(bandwith_list1)
    s2 = pd.Series(bandwith_list2)
    #create a plot with 2 subplots 
    fig, axes = plt.subplots(1, 2,figsize=(10,6))

    # configuration of plot 1 
    s1.plot(ax=axes[0],kind='line')
    s2.plot(ax=axes[0],kind='line')
    axes[0].set_xlabel('Time in s')
    axes[0].set_ylabel('Throughput in Mbit/s')
    

    #configuration of plot 2
    s1.plot(ax=axes[1],kind='kde')
    s2.plot(ax=axes[1],kind='kde')
    axes[1].set_xlabel('Throughput in Mbit/s')
    axes[1].set_ylabel('Density')
    plt.xlim(50, 150)
    plt.legend(['UE1','UE2'],loc="upper right")
    fig.savefig("../Pictures/Bandwith_iperf.pdf")
    print(s1.describe(), s2.describe())

def pandas3(bandwith_list1,bandwith_list2,bandwith_list3):
    s1 = pd.Series(bandwith_list1)
    s2 = pd.Series(bandwith_list2)
    s3 = pd.Series(bandwith_list3)
    fig, axes = plt.subplots(1, 2,figsize=(10,6))

    # configuration of plot 1 
    s1.plot(ax=axes[0],kind='line')
    s2.plot(ax=axes[0],kind='line')
    s3.plot(ax=axes[0],kind='line')
    axes[0].set_xlabel('Time in s')
    axes[0].set_ylabel('Throughput in Mbit/s')
    

    #configuration of plot 2
    s1.plot(ax=axes[1],kind='kde')
    s2.plot(ax=axes[1],kind='kde')
    s3.plot(ax=axes[1],kind='kde')
    
    axes[1].set_xlabel('Throughput in Mbit/s')
    axes[1].set_ylabel('Density')
    plt.xlim(40, 90)
    plt.legend(['UE1','UE2','UE3'],loc="upper right")
    fig.savefig("../Pictures/Bandwith_iperf.pdf")
    

   

    print(s1.describe(), s2.describe(), s3.describe())



file_paths=[
'../iperf5G_100.txt',
'../iperf5G_100_2.txt',
'../iperf5G66.txt',      
]

all_lists=[bandwith_list1,bandwith_list2,bandwith_list3]
#extract_mbits_per_sec1(file_path1)
#extract_mbits_per_sec2(file_path2)
#extract_mbits_per_sec3(file_path3)
extract_troughput(file_paths,all_lists)
#pandas(bandwith_list1)
pandas2(bandwith_list1,bandwith_list2)
#pandas3(bandwith_list1,bandwith_list2,bandwith_list3)

