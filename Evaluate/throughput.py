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
maximum_bandwith=[50,60,70,75,80,85,90]
csa_list=[]

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
                    bandwith_list3.append(bandwith)
            del bandwith_list3[-2:]
    return bandwith_list3

def pandas(bandwith_list1):
    s1 = pd.Series(bandwith_list1)

   #create a plot with 2 subplots 
    fig, axes = plt.subplots(1, 2,figsize=(10,6))

    # configuration of plot 1 
    s1.plot(ax=axes[0],kind='line')
    axes[0].set_title('Line Plot')
    axes[0].set_xlabel('Time in s')
    axes[0].set_ylabel('Throughput in Mbits')
    

    #configuration of plot 2
    s1.plot(ax=axes[1],kind='kde')
    axes[1].set_title('KDE Plot')
    axes[1].set_xlabel('Throughput in Mbits')
    axes[1].set_ylabel('Density')
    plt.xlim(120, 170)
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
    axes[0].set_title('Line Plot')
    axes[0].set_xlabel('Time in s')
    axes[0].set_ylabel('Throughput in Mbits')
    

    #configuration of plot 2
    s1.plot(ax=axes[1],kind='kde')
    s2.plot(ax=axes[1],kind='kde')
    axes[1].set_title('KDE Plot')
    axes[1].set_xlabel('Throughput in Mbits')
    axes[1].set_ylabel('Density')
    plt.xlim(0, 80)
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
    axes[0].set_title('Line Plot')
    axes[0].set_xlabel('Time in s')
    axes[0].set_ylabel('Throughput in Mbits')
    

    #configuration of plot 2
    s1.plot(ax=axes[1],kind='kde')
    s2.plot(ax=axes[1],kind='kde')
    s3.plot(ax=axes[1],kind='kde')
    
    axes[1].set_title('KDE Plot')
    axes[1].set_xlabel('Throughput in Mbits')
    axes[1].set_ylabel('Density')
    plt.xlim(0, 80)
    plt.legend(['UE1','UE2','UE3'],loc="upper right")
    fig.savefig("../Pictures/Bandwith_iperf.pdf")
    

    print(s1.describe())
    print(s2.describe())
    print(s3.describe())

    print(s1.describe(), s2.describe(), s3.describe())


file_path1 = '../iperf1.txt'
file_path2 = '../iperf2.txt'
file_path3 = '../iperf3.txt'

extract_mbits_per_sec1(file_path1)
extract_mbits_per_sec2(file_path2)
extract_mbits_per_sec3(file_path3)
#pandas(bandwith_list1)
#pandas2(bandwith_list1,bandwith_list2)
pandas3(bandwith_list1,bandwith_list2,bandwith_list3)
