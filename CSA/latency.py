import re
import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt 
import matplotlib as mpl
from scipy.stats import gaussian_kde
mpl.style.use('ggplot')
import seaborn as sns


latency_list= []
CSA_list= []
maximum_latency =[5,10,20,30,40,50,60,70,80,90]
file_path = 'ping.txt'


def extract_latency_from_ping(file_path):
    #This function extracts the latency from a ping.txt file
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                # i dont know, google it. filters the latency part out of the ping.txt file
                match = re.search(r"time=(\d+\.?\d*)", line)
                if match:
                    # attach the value to the var = latency
                    latency = float(match.group(1))
                    # append latency to an list
                    latency_list.append(latency)       
    except FileNotFoundError:
        print(f"Die Datei '{file_path}' wurde nicht gefunden.")
    return latency_list

def calculate_cas(latency_list):
    #This function calculates the CSA and adds it to an list
    counter = 0
    CSA = 0
    
    list_length = len(latency_list)
    
    #compare the meassured latency with the maximum latency for CSA
    for j in maximum_latency:
        # check for each latency if its higher or lower then the selected maximum latency and if its lower, increase counter by 1
        for i in latency_list:
            if i < j:
                counter +=1

        # Calculate the CAS by dividing the counter (Latency below maximum latency)   and total amount of elements  
        CSA = counter / list_length
        #add the calculated CSA to a list and multiply by 100 to get Percentage
        
        CSA_list.append(CSA*100)
        print('The CSA for a Maximum Latency of',j,'is:', CSA)
        counter = 0
    return CSA_list


def pandas(latency_list):
# This function creates a pandas series and creates plot of latency list and also a KDE    


    # Save the latency_list in a panda series
    s = pd.Series(latency_list)

    #create a plot with 2 subplots 
    fig, axes = plt.subplots(1, 2,figsize=(10,6))

    # configuration of plot 1 
    s.plot(ax=axes[0],kind='line')
    axes[0].set_title('Line Plot')
    axes[0].set_xlabel('Ping Count')
    axes[0].set_ylabel('Latency in ms')
    

    #configuration of plot 2
    s.plot(ax=axes[1],kind='kde')
    axes[1].set_title('KDE Plot')
    axes[1].set_xlabel('Latency in ms')
    axes[1].set_ylabel('Density')
    plt.xlim(-10, 150)

    # make it fit better
    plt.tight_layout()

    
    # save the plot as pdf
    fig.savefig("../Pictures/Latency_ping.pdf")
    
    # calculate statistic datas for latency_list
    print(s.describe())


def CSA_Plot(x_axis,y_axis):
    #plot figure and save it
    fig = plt.figure(figsize =(10, 7))
    plt.plot(x_axis,y_axis)
    plt.ylabel('CSA in %')
    plt.xlabel('maximum latency in ms')
    plt.savefig("../Pictures/CSA_Latency_Plot.png")


def BoxPlot_Latency(data):
    fig = plt.figure(figsize =(10, 7))
    plt.boxplot(data)
    plt.ylabel('Latency in ms')
    plt.savefig("../Pictures/CSA_Latency_BoxPlot.png")


#comment out the functions you need
extract_latency_from_ping(file_path)
#calculate_cas(latency_list)
#CSA_Plot(maximum_latency,CSA_list)
#BoxPlot_Latency(latency_list)
pandas(latency_list)
