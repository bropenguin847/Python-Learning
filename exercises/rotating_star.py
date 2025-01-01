"""
Plot a star with matplotlib
Rotate the star around 4 points
Show the result by plotting
*bonus points if animation
"""

import matplotlib.pyplot as plt
import numpy as np

# Star coordinates
x = [1, 3, 5, 1, 5, 1]
y = [1, 5, 1, 3.5, 3.5, 1]
plt.plot(x, y, '-b*')
plt.axis([0, 6, 0, 6])
plt.title('Star')
plt.show()
