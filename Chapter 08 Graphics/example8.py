"""
Chapter 8 Example 8
Stem plot
"""

import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 101)
w = 0.04 * np.pi
y = np.sin(w * n)
plt.stem(n, y)
plt.xlabel('sample, n')
plt.ylabel('sin(ω n)')
title = f'Discrete Sinusoidal Signal for $\\omega = {w/np.pi:.2f} \\pi$'
plt.title(title)
plt.show()
