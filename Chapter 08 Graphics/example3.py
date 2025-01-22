"""
Chapter 8 Example 3
"""

import numpy as np
import matplotlib.pyplot as plt
w = np.linspace(0, 2*np.pi, 1000)
y = np.sin(w)
plt.xlabel(r'$\omega$')
plt.ylabel(r'$\sin(\omega)$')
plt.title(r'Sin($\omega$) Graph')
ticks = [0, 0.5 * np.pi, np.pi, 1.5 * np.pi, 2 * np.pi]
tick_labels = ["0", r"$0.5\pi$", r"$\pi$", r"$1.5\pi$", r"$2\pi$"]
fig, ax = plt.subplots()
ax.plot(w, y)
ax.set_xticks(ticks)
ax.set_xticklabels(tick_labels)
plt.grid(True)
plt.show()
