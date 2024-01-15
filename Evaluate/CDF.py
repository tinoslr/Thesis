import re
import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt 
import matplotlib as mpl
mpl.style.use('ggplot')
import seaborn as sns
from scipy.stats import gaussian_kde



file_paths=[
'../ping66.txt',
'../MA5bUE.txt',
'../MA5cUE.txt',
'../MA5dUE.txt',
'../MA5eUE.txt'     
]



bandwith_list1=[]
bandwith_list2=[]
bandwith_list3=[]
bandwith_list4=[]
bandwith_list5=[]

all_lists=[bandwith_list1]

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

def pandas(bandwith_list1):
    # Erstelle ein Pandas DataFrame
    df = pd.DataFrame(bandwith_list1, columns=['Values'])

    # Berechne die CDF
    cdf = df['Values'].value_counts(normalize=True).sort_index().cumsum()

    # Plot der CDF
    plt.plot(cdf.index, cdf.values, linestyle='-', color='b')
    plt.title('Cumulative Distribution Function (CDF)')
    plt.xlabel('Values')
    plt.ylabel('CDF')
    plt.show()
    plt.savefig("../Pictures/CDF.pdf")

extract_troughput(file_paths,all_lists)
pandas(bandwith_list1)