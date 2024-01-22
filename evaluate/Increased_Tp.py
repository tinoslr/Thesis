import re
import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt 
import matplotlib as mpl
from scipy.stats import gaussian_kde
mpl.style.use('ggplot')
import seaborn as sns


offered_tp1=[50,100,150,200,250,300,350,400,500,600]
received_tp1=[50,100,149.3,200,215,216,212,216,214,215]

offered_tp2=[50,100,150,200,250,300,400,500,600]
received_tp2=[50,99.67,100.35,74.3,75.7,76.2,74.5,77.6,75.3]


   


def pandas(list1,list2,list3,list4):
# This function creates a pandas series and creates plot of latency list and also a KDE    
    # for i in range(len(list1)):
    #     list1[i]=list1[i]//60
    #     list2[i]=list2[i]//60
    # print(list1,list2)

    # Save the latency_list in a panda series
    fig = plt.figure(figsize =(10, 7))
    plt.plot(list1,list2)
    plt.plot(list3,list4)
    plt.ylabel('Received Throughput in Mbit/s', color = 'black')
    plt.xlabel('Offered Traffic in Mbit/s', color= 'black')
    plt.ylim(40,230)
    plt.tick_params(axis='x', colors='black')
    plt.tick_params(axis='y', colors='black')
    plt.legend(['P5G','WLAN'],loc="lower right")
    plt.savefig("../Pictures/Increased_TP.pdf")
    plt.savefig("../Pictures/Increased_TP.png")
    



pandas(offered_tp1,received_tp1,offered_tp2,received_tp2)