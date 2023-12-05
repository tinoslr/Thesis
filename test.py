import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('testdata.csv')
print(data.head())

korrelation = data['Latenz'].corr(data['Anzahl_Clients'])

print(f"Korrelation zwischen Latenz und Anzahl der Clients: {korrelation}")
fig, axes = plt.subplots(1, 2,figsize=(10,6))
plt.scatter(data['Anzahl_Clients'], data['Latenz'])
plt.xlabel('Anzahl der Clients')
plt.ylabel('Latenz')
plt.title('Korrelation zwischen Latenz und Anzahl der Clients')
fig.savefig("Bandwith_iperf.pdf")