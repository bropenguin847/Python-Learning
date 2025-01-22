"""
Plot a star with matplotlib
Rotate the star around 4 points
Show the result by plotting
*bonus points if animation
"""

import matplotlib.pyplot as plt
import numpy as np

# Star coordinates
x = [1, 2.5, 4, 1, 4, 1]
y = [1, 4.5, 1, 3, 3, 1]
plt.plot(x, y, '-b*')
plt.axis([0, 5, 0, 5.5])
plt.title('Star')
plt.show()
