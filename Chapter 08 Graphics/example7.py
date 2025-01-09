import numpy as np 
import matplotlib.pyplot as plt 

t = np.arange(0, 1.001, 0.001) 
for F in range(1, 5):
    y = np.sin(2 * np.pi * F * t)
    plt.subplot(2, 2, F)
    plt.plot(t, y)
    plt.xlabel('Time, t (s)')
    plt.ylabel(f'sin(2π({F})t)')
    plt.title(f'{F} Cycle')

plt.tight_layout() 
plt.show()
