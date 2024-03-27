import re
import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt 
import matplotlib as mpl
from scipy.stats import gaussian_kde
mpl.style.use('ggplot')


distance=[5,10,15,30,35]
received_throughput=[225,180,150,30,0]
distance2=[5,15,30,40,50]
received_throughput2=[225,220,207,105,70]




def pandas(list1,list2,list3,list4):
# This function creates a pandas series and creates plot of latency list and also a KDE    
    # for i in range(len(list1)):
    #     list1[i]=list1[i]//60
    #     list2[i]=list2[i]//60
    # print(list1,list2)
   
    d1 = {'TP': list1, 'DIS': list2}
    d2 = {'TP': list3, 'DIS': list4}
    #d2 = {'LT' : list3, 'DIS': list2}
    df1 = pd.DataFrame(data=d1)
    df2 = pd.DataFrame(data=d2)


    print(df1)
    print(df2)
    fig, ax = plt.subplots()
    # fig, axes = plt.subplots(1, 2,figsize=(10,6))
    df1.plot(ax=ax,x='DIS', y='TP', kind='line', color ='b')
    df2.plot(ax=ax,x='DIS', y='TP', kind='line', color ='r')
    
    
    ax.legend(['WLAN','P5G'],loc="upper right")
    ax.set_xlabel('Distance in Meter', color ='black')
    ax.set_ylabel('Throughput in Mbit/s', color ='black')
    ax.tick_params(axis='x', colors='black')
    ax.tick_params(axis='y', colors='black')
    ax.set_xlim(0, 55)
    ax.set_ylim(0,230)
    # df2.plot(x='DIS', y='LT', ax=axes[1], kind='line')
    # axes[1].legend().set_visible(False)
    # axes[1].set_xlabel('Distance in Meter')
    # axes[1].set_ylabel('Latency  in ms')

    fig.savefig("../Pictures/Distance.pdf")
    fig.savefig("../Pictures/Distance.png")



pandas(received_throughput,distance,received_throughput2,distance2)