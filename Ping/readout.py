import re
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


latency_list= []
CSA_list= []
maximum_latency =[20,30,40,50,60,70,80,90]
file_path = 'ping.txt'


def extract_latency_from_ping(file_path):
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

def save_plot(x_axis,y_axis):
    #plot figure and save it
    plt.plot(x_axis,y_axis)
    plt.ylabel('CSA in %')
    plt.xlabel('maximum latency in ms')
    plt.savefig("matplotlib.png")


extract_latency_from_ping(file_path)
calculate_cas(latency_list)
save_plot(maximum_latency,CSA_list)
