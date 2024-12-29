import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# Define a vector of nonuniform sample points and evaluate the sine function over the points
x1 = np.arange(-4*np.pi, 0, 0.1)
x2 = np.arange(0.1, 4*np.pi, 0.2)
x = np.concatenate([x1, x2])
A = np.sin(x)

# Inject outliers by making one peak very high and one dip very low
A[100] = 2  # Set a very high outlier at one peak
A[120] = 1.3  # Set a moderate outlier at one peak
A[170] = -2  # Set a very low outlier at one dip

# Create subplots (top: original data with outliers, bottom: data after outlier handling)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

# Plot the original data with outliers before replacing them
ax1.scatter(x, A, label='Original Data with Outliers', color='blue')
ax1.set_title("Original Data with Outliers")
ax1.legend()

# Detect the outliers (values > 1 or < -1)
outliers = (A > 1) | (A < -1)
A[outliers] = np.nan  # Replace outliers with NaN

# Fill the outlier (NaN) data using linear interpolation
F = np.copy(A)
nans = np.isnan(A)
F[nans] = np.interp(x[nans], x[~nans], A[~nans])

# Plot the filled data after replacing outliers
ax2.scatter(x, A, label='Data After Replacing Outliers with NaN', color='blue')
ax2.scatter(x[nans], F[nans], label='Filled Data (Outliers Replaced)', color='red')
ax2.set_title("Data After Outliers Replaced with Interpolation")
ax2.legend(loc='lower right')

plt.tight_layout()
plt.show()