"""
Chapter 8 Example 10
Magnitude vs Frequency (Log Scale)
"""

import numpy as np
import matplotlib.pyplot as plt

# Given values
C = 0.47e-6  # capacitance in Farads
R = 4.7e3    # resistance in Ohms
f = np.linspace(1, 10000, 10000)  # frequency range from 1 Hz to 10 kHz (using 1 instead of 0 to avoid log(0))

# Transfer function H(jw)
H = 1 / (1 + 1j * 2 * np.pi * f * R * C)

# Magnitude and Phase calculations
Magnitude = 20 * np.log10(np.abs(H))  # Magnitude in dB
Phase = np.angle(H)

# Subplot 1: Magnitude plot using semilogx
plt.subplot(2, 1, 1)
plt.semilogx(f, Magnitude)
plt.xlabel('Frequency, f (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title('Magnitude vs Frequency (Log Scale)')

# Subplot 2: Phase plot using semilogx
plt.subplot(2, 1, 2)
plt.semilogx(f, Phase / np.pi)
plt.xlabel('Frequency, f (Hz)')
plt.ylabel('Phase (π radians)') 
plt.yticks(np.arange(-1, 1.5, 0.5), [f'{tick:.1f}π' for tick in np.arange(-1, 1.5, 0.5)])

plt.tight_layout()
plt.show()
