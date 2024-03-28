from extractthroughput import extract
from plots import pandas1, pandas2, pandas3, pandas4, pandas5

# Create the bandwidth list to store the extracted throughput data for each device
bandwith_list1=[]
bandwith_list2=[]
bandwith_list3=[]
bandwith_list4=[]
bandwith_list5=[]

#nest all lists in one list. Usefull for the extract function. 
all_lists=[bandwith_list1,bandwith_list2,bandwith_list3,bandwith_list4,bandwith_list5]

file_paths=[]

def perform_plotting(number_of_devices):

    # Each key represents the number of devices to be plotted, while the corresponding value represents the function.
    nmb = {
        1: pandas1,
        2: pandas2,
        3: pandas3,
        4: pandas4,
        5: pandas5
    }
    # same here. Corresponding value represents number of lists needed for the plot.
    lists = {
        1: [bandwith_list1],
        2: [bandwith_list1, bandwith_list2],
        3: [bandwith_list1, bandwith_list2, bandwith_list3],
        4: [bandwith_list1, bandwith_list2, bandwith_list3, bandwith_list4],
        5: [bandwith_list1, bandwith_list2, bandwith_list3, bandwith_list4,bandwith_list5]
    }
    
    #combine everything 
    chosen_number_of_devices = nmb.get(number_of_devices)
    chosen_lists= lists.get(number_of_devices)
    #the * chosen list into seperate the list into seperate lists.
    chosen_number_of_devices(*chosen_lists)






# Input for number of devices     
x = int(input('How many devices need to be plotted? '))

# create the file paths list 
# store all txt-Files inside the txtfiles folder.
# Enter the needed name of the file. Filetyp is not needed
for i in range(x):
    file_paths.append('../txtfiles/'+ input('Name of the txtfile ' + str(i+1) + ': ') + '.txt')

# extracts the Throughput from each file
extract(file_paths,all_lists)
perform_plotting(x)


