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
bandwith_list4=[]
bandwith_list5=[]



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
                            if bandwith > 20:
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
    plt.xlim(120, 300)
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
    plt.xlim(20, 130)
    plt.legend(['UE1','UE2','UE3'],loc="upper right")
    fig.savefig("../Pictures/Bandwith_iperf.pdf")
    

   

    print(s1.describe(), s2.describe(), s3.describe())

def pandas4(bandwith_list1,bandwith_list2,bandwith_list3,bandwith_list4):
    s1 = pd.Series(bandwith_list1)
    s2 = pd.Series(bandwith_list2)
    s3 = pd.Series(bandwith_list3)
    s4 = pd.Series(bandwith_list4)
    fig, axes = plt.subplots(1, 2,figsize=(10,6))

    # configuration of plot 1 
    s1.plot(ax=axes[0],kind='line')
    s2.plot(ax=axes[0],kind='line')
    s3.plot(ax=axes[0],kind='line')
    s4.plot(ax=axes[0],kind='line')
    axes[0].set_xlabel('Time in s')
    axes[0].set_ylabel('Throughput in Mbit/s')
    

    #configuration of plot 2
    s1.plot(ax=axes[1],kind='kde')
    s2.plot(ax=axes[1],kind='kde')
    s3.plot(ax=axes[1],kind='kde')
    s4.plot(ax=axes[1],kind='kde')

    axes[1].set_xlabel('Throughput in Mbit/s')
    axes[1].set_ylabel('Density')
    plt.xlim(0, 130)
    plt.legend(['UE1','UE2','UE3','UE4'],loc="upper right")
    fig.savefig("../Pictures/Bandwith_iperf.pdf")
    

   

    print(s1.describe(), s2.describe(), s3.describe(),s4.describe())

def pandas5(bandwith_list1,bandwith_list2,bandwith_list3,bandwith_list4,bandwith_list5):
    s1 = pd.Series(bandwith_list1)
    s2 = pd.Series(bandwith_list2)
    s3 = pd.Series(bandwith_list3)
    s4 = pd.Series(bandwith_list4)
    s5 = pd.Series(bandwith_list5)
    fig, axes = plt.subplots(1, 2,figsize=(10,6))

    # configuration of plot 1 
    s1.plot(ax=axes[0],kind='line')
    s2.plot(ax=axes[0],kind='line')
    s3.plot(ax=axes[0],kind='line')
    s4.plot(ax=axes[0],kind='line')
    s5.plot(ax=axes[0],kind='line')
    axes[0].set_xlabel('Time in s')
    axes[0].set_ylabel('Throughput in Mbit/s')
    

    #configuration of plot 2
    s1.plot(ax=axes[1],kind='kde')
    s2.plot(ax=axes[1],kind='kde')
    s3.plot(ax=axes[1],kind='kde')
    s4.plot(ax=axes[1],kind='kde')
    s5.plot(ax=axes[1],kind='kde')
    axes[1].set_xlabel('Throughput in Mbit/s')
    axes[1].set_ylabel('Density')
    plt.xlim(0, 130)
    plt.legend(['UE1','UE2','UE3','UE4','UE5'],loc="upper right")
    fig.savefig("../Pictures/Bandwith_iperf.pdf")
    

   

    print(s1.describe(), s2.describe(), s3.describe(),s4.describe(),s5.describe())

file_paths=[
'../1UE5G.txt',
'../M4b.txt',
'../M4c.txt',
'../M4d.txt',
'../MA5eUE.txt'     
]

all_lists=[bandwith_list1,bandwith_list2,bandwith_list3,bandwith_list4,bandwith_list5]
extract_troughput(file_paths,all_lists)
pandas(bandwith_list1)
#pandas2(bandwith_list1,bandwith_list2)
#pandas3(bandwith_list1,bandwith_list2,bandwith_list3)
#pandas4(bandwith_list1,bandwith_list2,bandwith_list3,bandwith_list4)
#pandas5(bandwith_list1,bandwith_list2,bandwith_list3,bandwith_list4,bandwith_list5)

