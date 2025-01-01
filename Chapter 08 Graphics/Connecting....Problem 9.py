# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:11:39 2024

@author: ASUS
"""

import numpy as np
import matplotlib.pyplot as plt



C = 1e-6 
R = 10e3 
f = np.linspace(1, 10e4, 10) 


H = 1 / (1 + 1j * 2 * np.pi * f * R * C) 
Magnitude = 20 * np.log10(np.abs(H)) 
Phase = np.angle(H)

#Magnitude plot 
plt.subplot(2, 1, 1)
plt.semilogx(f, Magnitude)
plt.xlabel('Frequency, f (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title('Magnitude over Frequency,f (Hz) ')

#Phase plot
plt.subplot(2, 1, 2)
plt.semilogx(f, Phase / np.pi)
plt.xlabel('Frequency, f (Hz)')
plt.ylabel('Phase (π rad)')
plt.yticks(np.arange(-1, 1.5, 0.5), [f'{tick:.1f}π' for tick in np.arange(-1, 1.5, 0.5)])
plt.tight_layout()
plt.show()