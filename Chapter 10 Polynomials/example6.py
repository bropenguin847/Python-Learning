"""
Chapter 10 Example 6
This is related to example 5
To understand the system, the poly is evaluated over a range of s values.
Lastly, matplotlib.pyplot is used to plot a graph for visualizing system response.
"""

import numpy as np
import matplotlib.pyplot as plt

# Given Q_n and Q_d from previous calculation
Q_n = [2, 4, 1]  # Numerator: 2s^2 + 4s + 1
Q_d = [1, -2, 0]  # Denominator: s^2 - 2s

# Define frequency range (1 mHz to 10 kHz) with logarithmic spacing
frequencies = np.logspace(-3, 4, 1000)  # 1000 points from 1e-3 Hz to 1e4 Hz
omega = 2 * np.pi * frequencies  # Convert frequency to angular frequency (rad/s)
s = 1j * omega  # s = jω

# Evaluate the transfer function Q(s) = Q_n / Q_d over the frequency range
numerator = np.polyval(Q_n, s)
denominator = np.polyval(Q_d, s)
np.polyval(x,)

# Directly compute Q_s = Q_n / Q_d without handling zero-division
Q_s = numerator / denominator

# Plot frequency vs magnitude (|Q(s)|) with frequency on a logarithmic scale
plt.figure()
plt.semilogx(frequencies, np.abs(Q_s))  # Use semilogx for log frequency axis
plt.title("Frequency Response of Q(s)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude |Q(s)|")
plt.grid(True, which="both")  # Add grid lines for both major and minor
