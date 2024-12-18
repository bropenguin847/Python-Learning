#import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Load the reduced ECG data from the CSV file
reduced_ecg_data = pd.read_csv('reduced_ecg_signal.csv')

# Extract time and amplitude from the reduced CSV data
time_reduced = reduced_ecg_data['Time(s)'].values
amplitude_reduced = reduced_ecg_data['Amplitude'].values

# Interpolation using spline method (cubic)
spline_interpolation = interp1d(time_reduced, amplitude_reduced, kind='cubic')

# Increase sampling rate (e.g., 10 times higher)
new_time_high = np.linspace(time_reduced.min(), time_reduced.max(), len(time_reduced) * 10)

# Interpolated signal
new_amplitude_high = spline_interpolation(new_time_high)

# Plot the original and interpolated signals
plt.figure(figsize=(10, 6))

# Plot original reduced signal with markers
plt.plot(time_reduced, amplitude_reduced, 'o-', label='Reduced Sampling Signal', markersize=5)

# Plot interpolated signal
plt.plot(new_time_high, new_amplitude_high, '-', label='Interpolated Signal (Higher Sampling Rate)', alpha=0.8)

# Adding labels and title
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Comparison of Reduced and Interpolated ECG Signal')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
