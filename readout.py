import re

latency_list= []

def extract_latency_from_ping(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                match = re.search(r"time=(\d+\.?\d*)", line)
                if match:
                    latency = float(match.group(1))
                    latency_list.append(latency)       
    except FileNotFoundError:
        print(f"Die Datei '{file_path}' wurde nicht gefunden.")
    return latency_list

def calculate_cas(latency_list):
    counter = 0
    list_length = len(latency_list)
    CSA = 0
    for i in latency_list:
        if i < 20:
            counter +=1
    CSA = counter / list_length
    return print('The CSA is:', CSA)



file_path = 'ping.txt'
extract_latency_from_ping(file_path)
calculate_cas(latency_list)