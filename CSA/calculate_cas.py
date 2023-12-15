import re
import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt 
import matplotlib as mpl
mpl.style.use('ggplot')

latency_list= []
CSA_list= []
maximum_latency =[5,10,20,30,40,50,60,70,80,90]



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




def extract_troughput(filepaths,all_lists):

    for filepath, current_list in zip(filepaths,all_lists):
        with open(filepath, 'r') as file:
                lines = file.readlines()
                for i, line in enumerate(lines, start=1):
                    # i dont know, google it. filters the bandwith part out of the ping.txt file
                    match = re.search(r'(\d+(\.\d+)?)\s(M|)bits/sec', line)
                    if match:
                        # attach the value to the var = latency
                        bandwith = float(match.group(1))
                        if bandwith > 2:
                        # append throughput to an list
                            current_list.append(bandwith)
                    

                del current_list[-2:]
    return

def pandas2(bandwith_list1,bandwith_list2):
    s1 = pd.Series(bandwith_list1)
    s2 = pd.Series(bandwith_list2)
    #create a plot with 2 subplots 
    fig, axes = plt.subplots(1, 2,figsize=(10,6))

    # configuration of plot 1 
    s1.plot(ax=axes[0],kind='line')
    s2.plot(ax=axes[1],kind='line')
    
    axes[0].set_xlabel('Time in s')
    axes[0].set_ylabel('Throughput in Mbit/s')
   
    axes[1].set_xlabel('Time in s')
    axes[1].set_ylabel('Throughput in Mbit/s')
    
    fig.savefig("../CAS.pdf")
    print(s1.describe(), s2.describe())


bandwith_list1=[]
bandwith_list2=[]
bandwith_list3=[]
all_lists=[bandwith_list1,bandwith_list2,bandwith_list3]
filepaths=["GBR.txt","default1.txt"]

#extract_latency_from_ping(file_path)
#calculate_cas(latency_list)
#CSA_Plot(maximum_latency,latency_list)
#BoxPlot_Latency(latency_list)
extract_troughput(filepaths,all_lists)
pandas2(bandwith_list1,bandwith_list2)
