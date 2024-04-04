import re


def extract(filepaths,all_lists):

    try:
        for filepath, current_list in zip(filepaths,all_lists):
            with open(filepath, 'r') as file:
                    lines = file.readlines()
                    for i, line in enumerate(lines, start=1):
                        # i dont know, google it. filters the bandwith part out of the ping.txt file
                        match = re.search(r'(\d+(\.\d+)?)\s(M|)bits/sec', line)
                        if match:
                            # attach the value to the var = latency
                            bandwith = float(match.group(1))
                            
                            if bandwith > 0:
                                current_list.append(bandwith)
                            
                             #append throughput to an list
                           
                        
    
                    del current_list[-2:]

    except FileNotFoundError:
        print(f"Die Datei '{filepath}' wurde nicht gefunden.")                
    return 