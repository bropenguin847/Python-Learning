""" Chapter 9 Example 1
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Define the data points
x1 = np.arange(0, 4)
x2 = np.arange(0, 3.2, 0.2)
y = np.array([0, 1, 1, 0])

# Create interpolation functions
xnearest = interp1d(x1, y, kind='nearest')
xlinear = interp1d(x1, y, kind='linear')
xspline = interp1d(x1, y, kind='cubic')  # 'cubic' for spline interpolation

# Interpolated values
ynearest_vals = xnearest(x2)
ylinear_vals = xlinear(x2)
yspline_vals = xspline(x2)

# Plot the results
plt.plot(x1, y, 'o', label='Original Points')
plt.plot(x2, ynearest_vals, '-x', label='Nearest')
plt.plot(x2, ylinear_vals, ':s', label='Linear')
plt.plot(x2, yspline_vals, '--*', label='Spline')

# Add labels and title
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('Interpolation Method')
plt.legend()

# Save the plot as a high-resolution vector file (SVG, EPS, or PDF)
plt.savefig('plot_high_res.svg', format='svg', dpi=600)  # Save as SVG
plt.savefig('plot_high_res.pdf', format='pdf', dpi=600)  # Save as PDF
# plt.savefig('plot_high_res.eps', format='ePS', dpi=600)  # Save as EPS

# Show the plot
plt.show()
