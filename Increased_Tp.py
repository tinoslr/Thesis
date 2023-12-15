import re
import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt 
import matplotlib as mpl
from scipy.stats import gaussian_kde
mpl.style.use('ggplot')
import seaborn as sns


offered_tp=[50,100,150,200,250,300,350,400,450]
received_tp=[50,99,149.3,199.5,224,226.9,225,225.9,227]


   


def pandas(list1,list2):
# This function creates a pandas series and creates plot of latency list and also a KDE    
    # for i in range(len(list1)):
    #     list1[i]=list1[i]//60
    #     list2[i]=list2[i]//60
    # print(list1,list2)

    # Save the latency_list in a panda series
    fig = plt.figure(figsize =(10, 7))
    plt.plot(list1,list2)
    plt.ylabel('Received Throughput in Mbit/s')
    plt.xlabel('Offered Traffic in Mbit/s')
    plt.savefig("Pictures/Increased_TP.pdf")


pandas(offered_tp,received_tp)