"""
scipy library is not used, put here as an example
for another library that have interpolate function
"""

import numpy as np
import matplotlib.pyplot as plt
# from scipy import interpolate

# Define a vector of nonuniform sample points and evaluate the sine function over the points
x1 = np.arange(-4*np.pi, 0, 0.1)
x2 = np.arange(0.1, 4*np.pi, 0.2)
x = np.concatenate([x1, x2])
A = np.sin(x)

# Inject NaN values into A (similar to the MATLAB condition A < 0.75 & A > 0.5)
A[(A < 0.75) & (A > 0.5)] = np.nan

# Fill the missing data using linear interpolation
F = np.copy(A)
nans = np.isnan(A)
F[nans] = np.interp(x[nans], x[~nans], A[~nans])

# Create subplots (top: original data with NaN values, bottom: data after filling NaN values)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

# Plot the original data with NaN values
ax1.scatter(x, A, label='Original Data with Missing Values', color='blue')
ax1.set_title("Original Data with Missing Values (NaN)")
ax1.legend(loc='lower left')

# Plot the data after filling NaN values with interpolation
ax2.scatter(x, A, label='Data After Filling Missing Values', color='blue')
ax2.scatter(x[nans], F[nans], label='Filled Data (Missing Values Replaced)', color='red')
ax2.set_title("Data After Filling Missing Values (Interpolation)")
ax2.legend(loc='lower left')

plt.tight_layout()
plt.show()
