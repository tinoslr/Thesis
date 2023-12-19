import re
import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt 
import matplotlib as mpl
from scipy.stats import gaussian_kde
mpl.style.use('ggplot')


distance=[5,10,20,30,50]
received_throughput=[199,200,200,199,87]
latency=[13.4,14.5,13.9,12.6,18.6]




def pandas(list1,list2,list3):
# This function creates a pandas series and creates plot of latency list and also a KDE    
    # for i in range(len(list1)):
    #     list1[i]=list1[i]//60
    #     list2[i]=list2[i]//60
    # print(list1,list2)
   
    d1 = {'TP': list1, 'DIS': list2}
    d2 = {'LT' : list3, 'DIS': list2}
    df1 = pd.DataFrame(data=d1)
    df2 = pd.DataFrame(data=d2)


    print(df1)
    fig, axes = plt.subplots(1, 2,figsize=(10,6))
    df1.plot(x='DIS', y='TP',ax=axes[0], kind='line')

    axes[0].legend().set_visible(False)
    axes[0].set_xlabel('Distance in Meter')
    axes[0].set_ylabel('Throughput in Mbit/s')

    df2.plot(x='DIS', y='LT', ax=axes[1], kind='line')
    axes[1].legend().set_visible(False)
    axes[1].set_xlabel('Distance in Meter')
    axes[1].set_ylabel('Latency  in ms')


    fig.savefig("../Pictures/Distance.pdf")


pandas(received_throughput,distance,latency)