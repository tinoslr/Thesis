import re
import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt 
import matplotlib as mpl
mpl.style.use('ggplot')
import seaborn as sns
from scipy.stats import gaussian_kde



file_paths=[
'../txtfiles/ping225.txt',
'../txtfiles/ping5G1.txt',
'../txtfiles/ping.txt',
'../txtfiles/ping5.txt',
'../MA5eUE.txt'     
]



bandwith_list1=[]
bandwith_list2=[]
bandwith_list3=[]
bandwith_list4=[]
bandwith_list5=[]

all_lists=[bandwith_list1,bandwith_list2,bandwith_list3,bandwith_list4]

def extract_troughput(filepaths,all_lists):
    try:
        for filepath, current_list in zip(filepaths,all_lists):
            with open(filepath, 'r') as file:
                    lines = file.readlines()
                    for i, line in enumerate(lines, start=1):
                        # i dont know, google it. filters the bandwith part out of the ping.txt file
                        match = re.search(r"time=(\d+\.?\d*)", line)
                        if match:
                            # attach the value to the var = latency
                            bandwith = float(match.group(1))
                            if bandwith > 0:
                            # append throughput to an list
                                current_list.append(bandwith)
                        
    
                    del current_list[-2:]
    except FileNotFoundError:
        print(f"Die Datei '{filepath}' wurde nicht gefunden.")                
    return 

def pandas(bandwith_list1,bandwith_list2):
    # Erstelle ein Pandas DataFrame
    df = pd.DataFrame(bandwith_list1, columns=['Values'])
    df2 = pd.DataFrame(bandwith_list2, columns=['Values'])
    
    # Berechne die CDF
    cdf = df['Values'].value_counts(normalize=True).sort_index().cumsum()
    cdf2 = df2['Values'].value_counts(normalize=True).sort_index().cumsum()
    
    # Plot der CDF
    plt.plot(cdf.index, cdf.values, linestyle='-', color='b')
    plt.plot(cdf2.index, cdf2.values, linestyle='-', color='r')
    plt.xlabel('Latency in ms', color='black')
    plt.ylabel('Probability', color='black')
    plt.tick_params(axis='x', colors='black')
    plt.tick_params(axis='y', colors='black')
    plt.legend(['WLAN','P5G'],loc="lower right")

    plt.savefig("../Pictures/CDF2.pdf")
    plt.savefig("../Pictures/CDF2.png")

def subpandas(bandwith_list1,bandwith_list2,bandwith_list3,bandwith_list4):
    # Erstelle ein Pandas DataFrame
    df = pd.DataFrame(bandwith_list1, columns=['Values'])
    df2 = pd.DataFrame(bandwith_list2, columns=['Values'])
    df3 = pd.DataFrame(bandwith_list3, columns=['Values'])
    df4 = pd.DataFrame(bandwith_list4, columns=['Values'])
    # Berechne die CDF
    cdf = df['Values'].value_counts(normalize=True).sort_index().cumsum()
    cdf2 = df2['Values'].value_counts(normalize=True).sort_index().cumsum()
    cdf3 = df3['Values'].value_counts(normalize=True).sort_index().cumsum()
    cdf4 = df4['Values'].value_counts(normalize=True).sort_index().cumsum()
    # Plot der CDF
    fig, axes = plt.subplots(1, 2,figsize=(10,6))

    axes[0].plot(cdf.index, cdf.values, linestyle='-', color='b')
    axes[0].plot(cdf2.index, cdf2.values, linestyle='-', color='r')
    axes[1].plot(cdf3.index, cdf3.values, linestyle='-', color='b')
    axes[1].plot(cdf4.index, cdf4.values, linestyle='-', color='r')
    axes[0].set_xlabel('Latency in ms', color='black')
    axes[0].set_ylabel('Probability', color='black')
    axes[1].set_xlabel('Latency in ms', color='black')
    axes[1].set_ylabel('Probability', color='black')
    axes[0].tick_params(axis='x', colors='black')
    axes[0].tick_params(axis='y', colors='black')
    axes[1].tick_params(axis='x', colors='black')
    axes[1].tick_params(axis='y', colors='black')
    axes[0].legend(['WLAN','P5G'],loc="lower right")
    axes[1].legend(['WLAN','P5G'],loc="lower right")

    plt.savefig("../Pictures/CDF2.pdf")
    plt.savefig("../Pictures/CDF2.png")


extract_troughput(file_paths,all_lists)
#pandas(bandwith_list1,bandwith_list2)
subpandas(bandwith_list1,bandwith_list2,bandwith_list3,bandwith_list4)