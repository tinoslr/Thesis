import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt 
import matplotlib as mpl
mpl.style.use('ggplot')
import seaborn as sns
from scipy.stats import gaussian_kde


def pandas1(bandwith_list1):
    s1 = pd.Series(bandwith_list1)

   #create a plot with 2 subplots 
    fig, axes = plt.subplots(1, 2,figsize=(10,6))

    # configuration of plot 1 
    s1.plot(ax=axes[0],kind='line')
    axes[0].set_xlabel('Time in s',color='black')
    axes[0].set_ylabel('Throughput in Mbit/s',color='black')
    axes[0].tick_params(axis='x', colors='black')
    axes[0].tick_params(axis='y', colors='black')
    print('For your information: The min value is '+ str(s1.min()) + 'and the max value is '+ str(s1.max()))
    axes[0].set_ylim(int(input('Y-Min für LinePlot: ')),int(input('Y-Max für Lineplot: ' )))
    
    #configuration of plot 2
    s1.plot(ax=axes[1],kind='kde')
    axes[1].set_xlabel('Throughput in Mbit/s',color='black')
    axes[1].set_ylabel('Density',color='black')
    axes[1].tick_params(axis='x', colors='black')
    axes[1].tick_params(axis='y', colors='black')
    axes[1].set_xlim(int(input('X-Min für KDE: ')),int(input('X-Max für KDE: ' )))
    axes[1].set_ylim(int(input('Y-Min für KDE: ')), int(input('Y-Max für KDE: ' )))

    
    plt.legend(['UE1'],loc="upper right")

    # make it fit better
    
    fig.savefig("../Pictures/BW_1UE.pdf")
    fig.savefig("../Pictures/BW_1UE.png")
    print(s1.describe())

def pandas2(bandwith_list1,bandwith_list2):
    s1 = pd.Series(bandwith_list1)
    s2 = pd.Series(bandwith_list2)
    #create a plot with 2 subplots 
    fig, axes = plt.subplots(1, 2,figsize=(10,6))

    # configuration of plot 1 
    s1.plot(ax=axes[0],kind='line')
    s2.plot(ax=axes[0],kind='line')
    axes[0].set_xlabel('Time in s',color='black')
    axes[0].set_ylabel('Throughput in Mbit/s',color='black')
    axes[0].tick_params(axis='x', colors='black')
    axes[0].tick_params(axis='y', colors='black')
    axes[0].set_ylim(int(input('Y-Min für LinePlot: ')),int(input('Y-Max für Lineplot: ' )))
    

    #configuration of plot 2
    s1.plot(ax=axes[1],kind='kde')
    s2.plot(ax=axes[1],kind='kde')
    axes[1].set_xlabel('Throughput in Mbit/s',color='black')
    axes[1].set_ylabel('Density',color='black')
    axes[1].tick_params(axis='x', colors='black')
    axes[1].tick_params(axis='y', colors='black')
    axes[1].set_xlim(int(input('X-Min für KDE: ')),int(input('X-Max für KDE: ' )))
    axes[1].set_ylim(int(input('Y-Min für KDE: ')), int(input('Y-Max für KDE: ' )))

    plt.legend(['UE1','UE2'],loc="upper right")
    fig.savefig("../Pictures/BW_2UE.png")
    fig.savefig("../Pictures/BW_2UE.pdf")
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
    axes[0].set_xlabel('Time in s',color='black')
    axes[0].set_ylabel('Throughput in Mbit/s',color='black')
    axes[0].tick_params(axis='x', colors='black')
    axes[0].tick_params(axis='y', colors='black')
    axes[0].set_ylim(int(input('Y-Min für LinePlot: ')),int(input('Y-Max für Lineplot: ' )))

    

    #configuration of plot 2
    s1.plot(ax=axes[1],kind='kde')
    s2.plot(ax=axes[1],kind='kde')
    s3.plot(ax=axes[1],kind='kde')
    axes[1].set_xlabel('Throughput in Mbit/s',color='black')
    axes[1].set_ylabel('Density',color='black')
    axes[1].tick_params(axis='x', colors='black')
    axes[1].tick_params(axis='y', colors='black')
    axes[1].set_xlim(int(input('X-Min für KDE: ')),int(input('X-Max für KDE: ' )))
    axes[1].set_ylim(int(input('Y-Min für KDE: ')), int(input('Y-Max für KDE: ' )))


    
    plt.legend(['UE1','UE2','UE3'],loc="upper right")
    fig.savefig("../Pictures/BW_3UE.png")
    fig.savefig("../Pictures/BW_3UE.pdf")
    

   

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
    axes[0].set_xlabel('Time in s',color='black')
    axes[0].set_ylabel('Throughput in Mbit/s',color='black')
    axes[0].tick_params(axis='x', colors='black')
    axes[0].tick_params(axis='y', colors='black')
    axes[0].set_ylim(int(input('Y-Min für LinePlot: ')),int(input('Y-Max für Lineplot: ' )))

    #configuration of plot 2
    s1.plot(ax=axes[1],kind='kde')
    s2.plot(ax=axes[1],kind='kde')
    s3.plot(ax=axes[1],kind='kde')
    s4.plot(ax=axes[1],kind='kde')
    axes[1].set_xlabel('Throughput in Mbit/s',color='black')
    axes[1].set_ylabel('Density',color='black')
    axes[1].tick_params(axis='x', colors='black')
    axes[1].tick_params(axis='y', colors='black')
    axes[1].set_xlim(int(input('X-Min für KDE: ')),int(input('X-Max für KDE: ' )))
    axes[1].set_ylim(int(input('Y-Min für KDE: ')), int(input('Y-Max für KDE: ' )))


    
    plt.legend(['UE1','UE2','UE3','UE4'],loc="upper right")
    fig.savefig("../Pictures/BW_4UE.png")
    fig.savefig("../Pictures/BW_4UE.pdf")
    

   

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
    axes[0].set_xlabel('Time in s',color='black')
    axes[0].set_ylabel('Throughput in Mbit/s',color='black')
    axes[0].tick_params(axis='x', colors='black')
    axes[0].tick_params(axis='y', colors='black')
    axes[0].set_ylim(int(input('Y-Min für LinePlot: ')),int(input('Y-Max für Lineplot: ' )))
    

    #configuration of plot 2
    s1.plot(ax=axes[1],kind='kde')
    s2.plot(ax=axes[1],kind='kde')
    s3.plot(ax=axes[1],kind='kde')
    s4.plot(ax=axes[1],kind='kde')
    s5.plot(ax=axes[1],kind='kde')
    axes[1].set_xlabel('Throughput in Mbit/s',color='black')
    axes[1].set_ylabel('Density',color='black')
    axes[1].tick_params(axis='x', colors='black')
    axes[1].tick_params(axis='y', colors='black')
    axes[1].set_xlim(int(input('X-Min für KDE: ')),int(input('X-Max für KDE: ' )))
    axes[1].set_ylim(int(input('Y-Min für KDE: ')), int(input('Y-Max für KDE: ' )))
    
    plt.legend(['UE1','UE2','UE3','UE4','UE5'],loc="upper right")
    fig.savefig("../Pictures/BW_5UE.png")
    fig.savefig("../Pictures/BW_5UE.pdf")
    

   

    print(s1.describe(), s2.describe(), s3.describe(),s4.describe(),s5.describe())