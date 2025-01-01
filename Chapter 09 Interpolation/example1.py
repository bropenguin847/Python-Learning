import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Define the data points
x = np.array([0, 1, 1, 0])
n1 = np.arange(0, 4)
n2 = np.arange(0, 3.2, 0.2)

# Create interpolation functions
xnearest = interp1d(n1, x, kind='nearest')
xlinear = interp1d(n1, x, kind='linear')
xspline = interp1d(n1, x, kind='cubic')  # 'cubic' for spline interpolation

# Interpolated values
xnearest_vals = xnearest(n2)
xlinear_vals = xlinear(n2)
xspline_vals = xspline(n2)

# Plot the results
plt.plot(n1, x, 'o', label='Original Points')
plt.plot(n2, xnearest_vals, '-x', label='Nearest')
plt.plot(n2, xlinear_vals, ':s', label='Linear')
plt.plot(n2, xspline_vals, '--*', label='Spline')

# Add labels and title
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('Interpolation Method')
plt.legend()

# Save the plot as a high-resolution vector file (SVG, EPS, or PDF)
# plt.savefig('plot_high_res.svg', format='svg', dpi=600)  # Save as SVG
plt.savefig('plot_high_res.pdf', format='pdf', dpi=600)  # Save as PDF
# plt.savefig('plot_high_res.eps', format='ePS', dpi=600)  # Save as EPS

# Show the plot
plt.show()