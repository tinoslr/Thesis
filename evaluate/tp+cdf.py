import re
import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt 
import matplotlib as mpl
mpl.style.use('ggplot')
import seaborn as sns
from scipy.stats import gaussian_kde



bandwith_list1 = []
bandwith_list2 = []
bandwith_list3 = []
all_lists=[bandwith_list1,bandwith_list2,bandwith_list3]

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
                            #if bandwith > 70:
                            #    bandwith = 60
                            if bandwith > 0:
                            # append throughput to an list
                                current_list.append(bandwith)
                        
    
                    del current_list[-2:]
    except FileNotFoundError:
        print(f"Die Datei '{filepath}' wurde nicht gefunden.")                
    return 

def createplot(bandwith_list1,bandwith_list2,bandwith_list3):
    s1 = pd.Series(bandwith_list1)
    s2 = pd.Series(bandwith_list2)
    s3 = pd.Series(bandwith_list3)
    df = pd.DataFrame(bandwith_list1, columns=['Values'])
    df2 = pd.DataFrame(bandwith_list2, columns=['Values'])
    df3 = pd.DataFrame(bandwith_list3, columns=['Values'])
    cdf = df['Values'].value_counts(normalize=True).sort_index().cumsum()
    cdf2 = df2['Values'].value_counts(normalize=True).sort_index().cumsum()
    cdf3 = df3['Values'].value_counts(normalize=True).sort_index().cumsum()


    fig, axes = plt.subplots(1, 2,figsize=(10,6))

    s1.plot(ax = axes[0], kind='line', color='red')
    s2.plot(ax = axes[0], kind='line',color='blue')
    s3.plot(ax = axes[0], kind='line', color='green')
    axes[0].set_xlabel('Time in s',color='black')
    axes[0].set_ylabel('Throughput in Mbit/s',color='black')
    axes[0].tick_params(axis='x', colors='black')
    axes[0].tick_params(axis='y', colors='black')
    axes[0].set_ylim(0,100)

    axes[1].plot(cdf.index, cdf.values, linestyle='-', color='r')
    axes[1].plot(cdf2.index, cdf2.values, linestyle='-', color='b')
    axes[1].plot(cdf3.index, cdf3.values, linestyle='-', color='g')
    axes[1].set_xlabel('Throughput in Mbit/s', color='black')
    axes[1].set_ylabel('Probability', color='black')
    axes[1].tick_params(axis='x', colors='black')
    axes[1].tick_params(axis='y', colors='black')
    axes[1].legend(['UE1','UE2','UE3'],loc="lower right")

    plt.savefig("../Pictures/TP+CDF.pdf")
    plt.savefig("../Pictures/TP+CDF.png")

    print(s1.describe(), s2.describe(), s3.describe())


filepaths=[
'../txtfiles/QoS1.txt',
'../txtfiles/Qosc.txt',
'../txtfiles/Qosd.txt'     
]

extract_troughput(filepaths,all_lists)
createplot(bandwith_list1,bandwith_list2,bandwith_list3)