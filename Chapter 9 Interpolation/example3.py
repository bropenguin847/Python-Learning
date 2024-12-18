import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, PchipInterpolator

# Given data from the table
x_values = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
y_values = np.array([0.00, 0.21, 0.38, 0.51, 0.62, 0.71, 0.79, 0.86, 0.91, 0.96, 1.0])

# Interpolation using spline and PCHIP methods
spline_interpolation = interp1d(x_values, y_values, kind='cubic')
pchip_interpolation = PchipInterpolator(x_values, y_values)

# Interpolating the value of y at x = 0.45
x_interp = 0.45
y_spline = spline_interpolation(x_interp)
y_pchip = pchip_interpolation(x_interp)

# Plot the VLE diagram
plt.figure(figsize=(8,6))
plt.plot(x_values, y_values, 'o', label='Data Points')
plt.plot(x_values, spline_interpolation(x_values), '--', label='Spline Interpolation')
plt.plot(x_values, pchip_interpolation(x_values), '-.', label='PCHIP Interpolation')

# Highlight the interpolated points for x = 0.45
plt.scatter(x_interp, y_spline, color='red', zorder=5, label=f'Spline y({x_interp})={y_spline:.2f}')
plt.scatter(x_interp, y_pchip, color='green', zorder=5, label=f'PCHIP y({x_interp})={y_pchip:.2f}')

plt.xlabel('Liquid Mole Fraction, x')
plt.ylabel('Vapor Mole Fraction, y')
plt.title('VLE Diagram for Benzene-Toluene at 1 atm')
plt.legend()
plt.grid(True)
plt.show()

# Output the interpolated values
print(f"Spline interpolation: y({x_interp}) = {y_spline:.5f}")
print(f"PCHIP interpolation: y({x_interp}) = {y_pchip:.5f}")
