'''
Problem 4 - 5 in  Asynchronous Class Activity.pdf
'''

import matplotlib.pyplot as plt
import numpy as np

temperatures = [15,17,19,21,23,25,27,28,27,26,24,22,20]
time = ['6AM', '7AM',  '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM',
        '3PM', '4PM', '5PM', '6PM']

##############################################################
t = np.arange(1, 11)
bacteria_num = 10
bacteria_growth = bacteria_num ** t

plt.subplot(121)
plt.stem(time, temperatures, '-.rx')
plt.title('Temperatures (°C) recorded hourly. Stem Plot')
plt.xticks(time, time)
plt.xlabel('Time')
plt.ylabel('Temperature')

plt.subplot(122)
plt.semilogy(t, bacteria_growth, '-mo')
plt.title('Logarithmic Plot')
plt.xlabel('Time, (hours)')
plt.xticks(t)
plt.ylabel('Bacterial Growth')
plt.tight_layout()
plt.show()
