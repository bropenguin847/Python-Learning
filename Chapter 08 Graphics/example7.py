"""
Chapter 8 Example 7
Multiple plotting using for loop
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 1.001, 0.001)
for index in range(1, 5):
    y = np.sin(2 * np.pi * index * t)
    plt.subplot(2, 2, index)
    plt.plot(t, y)
    plt.xlabel('Time, t (s)')
    plt.ylabel(f'sin(2π({index})t)')
    plt.title(f'{index} Cycle')

plt.tight_layout()
plt.show()
