import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, PchipInterpolator

# Load the DAC data from the CSV file
dac_data = pd.read_csv('dac_signal.csv')

# Extract time and amplitude from the CSV data
time = dac_data['Time(ms)'].values
amplitude = dac_data['Amplitude'].values

# Define the time points for interpolation (higher resolution)
time_interp = np.linspace(time.min(), time.max(), 50)

# Perform different interpolation methods
linear_interp = interp1d(time, amplitude, kind='linear')
nearest_interp = interp1d(time, amplitude, kind='nearest')
pchip_interp = PchipInterpolator(time, amplitude)
spline_interp = interp1d(time, amplitude, kind='cubic')

# Get the interpolated amplitudes for each method
amplitude_linear = linear_interp(time_interp)
amplitude_nearest = nearest_interp(time_interp)
amplitude_pchip = pchip_interp(time_interp)
amplitude_spline = spline_interp(time_interp)

# Create subplots for stem plots using plt.subplot
plt.figure(figsize=(12, 8))

# Linear interpolation subplot
plt.subplot(2, 2, 1)
plt.stem(time_interp, amplitude_linear, linefmt='-', markerfmt='o', basefmt='k')
plt.title('Linear Interpolation')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')

# Nearest interpolation subplot
plt.subplot(2, 2, 2)
plt.stem(time_interp, amplitude_nearest, linefmt='-', markerfmt='o', basefmt='k')
plt.title('Nearest Interpolation')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')

# PCHIP interpolation subplot
plt.subplot(2, 2, 3)
plt.stem(time_interp, amplitude_pchip, linefmt='-', markerfmt='o', basefmt='k')
plt.title('PCHIP Interpolation')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')

# Spline interpolation subplot
plt.subplot(2, 2, 4)
plt.stem(time_interp, amplitude_spline, linefmt='-', markerfmt='o', basefmt='k')
plt.title('Spline Interpolation')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')

# Adjust layout and show plot
plt.tight_layout()
plt.show()
