import re
import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt 
import matplotlib as mpl
from scipy.stats import gaussian_kde
mpl.style.use('ggplot')
import seaborn as sns


offered_tp=[22858,45714,68585,91457,114333,137286,159911,182868,201314]
received_tp=[22775,45717,68357,90946,89820,98179,114534,72869,53460]


   


def pandas(list1,list2):
# This function creates a pandas series and creates plot of latency list and also a KDE    
    for i in range(len(list1)):
        list1[i]=list1[i]//60
        list2[i]=list2[i]//60
    print(list1,list2)

    # Save the latency_list in a panda series
    fig = plt.figure(figsize =(10, 7))
    plt.plot(list1,list2)
    plt.ylabel('Received Throughput in Packets per Second')
    plt.xlabel('Offered Traffic in Packets per Second')
    plt.savefig("Pictures/Increased_TP.png")


pandas(offered_tp,received_tp)