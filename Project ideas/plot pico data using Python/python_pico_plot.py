#Title: Plot data from Raspberry Pi Pico using Python
#Author: Jude Nkereuwem
#Date: May, 2023


import matplotlib.pyplot as plt
import numpy as np
import serial
import time
import os

#Serial comm config
ser = serial.Serial('COM13', 115200)
time.sleep(2)

# Create empty lists to store x and y values
x_val = 0
x = []
y = []

# Create figure and axis objects
fig, ax = plt.subplots()
line, = ax.plot(x, y)

ax.set_xlabel('Time (s)')
ax.set_ylabel('Light intensity (%)')
ax.set_title('Real-time LDR plot')
plt.ion()
plt.show()


while True:

    #Read incomming data from Pico
    b = ser.readline().decode('ascii').strip()
    print("Brightness: ", b, "%")
    
    # Append values to lists
    x_val += 1
    x.append(x_val)
    y.append(int(b))

    #Graph plot
    line.set_xdata(x)
    line.set_ydata(y)
    ax.relim()
    ax.autoscale_view(True,True,True)
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.01)


ser.close()  
