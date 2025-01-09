import numpy as np
import matplotlib.pyplot as plt

# Given values
C = 0.47e-6  # capacitance in Farads
R = 4.7e3    # resistance in Ohms
f = np.linspace(0, 10000, 10000)  # frequency range from 0 to 10 kHz

# Transfer function H(jw)
H = 1 / (1 + 1j * 2 * np.pi * f * R * C)

# Magnitude and Phase of H
Magnitude = np.abs(H)
Phase = np.angle(H)

# Plotting the Magnitude and Phase
plt.figure(figsize=(10, 6))

# Subplot 1: Magnitude
plt.subplot(2, 1, 1)
plt.plot(f / 1000, Magnitude)
plt.xlabel('Frequency (kHz)')
plt.ylabel('Magnitude')
plt.xticks(np.arange(0, 11, step=2))  # Setting xticks every 2 kHz

# Subplot 2: Phase with custom π tick labels
plt.subplot(2, 1, 2)
plt.plot(f / 1000, Phase / np.pi)
plt.xlabel('Frequency (kHz)')
plt.ylabel('Phase ($\\pi$ rad)')

# Setting yticks as multiples of π
yticks = [-1, -0.5, 0, 0.5, 1]
ytick_labels = ['-1π', '-0.5π', '0π', '0.5π', '1.0π']
plt.yticks(yticks, ytick_labels)

plt.xticks(np.arange(0, 11, step=2))  # Setting xticks every 2 kHz
plt.tight_layout()
plt.show()
