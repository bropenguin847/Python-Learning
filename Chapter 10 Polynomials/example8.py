import numpy as np
import matplotlib.pyplot as plt

# Define constants
v = 30  # Initial velocity (m/s)
g = -9.8  # Acceleration due to gravity (m/s^2)

# Define the coefficients of the polynomial for displacement
# Corresponding to d = v*t + (g/2)*t^2
p = [g/2, v, 0]

# Find the roots of the polynomial
r = np.roots(p)

# The time when the object hits the ground (non-zero root)
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
