import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')



def save_plot(x_axis,y_axis):
    #plot figure and save it
    plt.grid(True)
    plt.plot(x_axis,y_axis, linestyle='dotted')
    plt.ylabel('Measured Troughput in Mbps')
    plt.xlabel('Expected Troughput in Mbps')
    plt.savefig("../Picutres/Iperf.png")


Expected_Troughput = [5,10,25,50,75,100,150,200,500]
Measured_Troughput = [5,9.89,24.7,31.7,13.2,14.6,1.16,3.98,0.50]

save_plot(Expected_Troughput,Measured_Troughput)