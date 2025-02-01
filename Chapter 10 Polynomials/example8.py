"""
Chapter 10 Example 8
Finding the roots, then evaulating and plotting
"""

import numpy as np
import matplotlib.pyplot as plt

# Define constants
v = 30      # Initial velocity (m/s)
g = -9.8    # Acceleration due to gravity (m/s^2)

# Define the coefficients of the polynomial for displacement
# Corresponding to d = v*t + (g/2)*t^2
p = [g/2, v, 0]

# Find the roots of the polynomial
r = np.roots(p)

# The time when the object hits the ground (non-zero root)
'''
This code below filters the roots to exclude 0,
assuming zero is not a valid solution for the specific problem.
[r != 0] is a boolean mask that is true for non-zero roots
r[r != 0]: Applies the mask to the array r, returning only the non-zero roots.
[0]: Selects the first non-zero root from the filtered array.
'''
tground = r[r != 0][0]

# Generate time values from 0 to tground
t = np.arange(0, tground, 0.01)

# Calculate displacement values
d = np.polyval(p, t)

# Plot the vertical displacement
plt.plot(t, d)
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.title('Vertical Displacement')
plt.show()
