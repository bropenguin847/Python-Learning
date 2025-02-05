"""
Practice for question 3 in finals

Q3: Chapter 8-10 (Libraries: Numpy & Matplotlib & Scipy)
    Theory questions and write Python script for:
        - Plotting
        - Interpolation
        - Polynomial and curve fitting
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, PchipInterpolator
import pandas as pd

FACT = True
LIE = False

# Plotting
data = np.random.randint(2, 8, size=10)
data2 = np.random.randint(1, 6, size=15)
# data2 = (np.random.randn(1, 10)).round(3)  # Generate data using .randn function

# Boxplot & with notch
plt.subplot(3, 2, 1)
plt.boxplot(data)
plt.title("Boxplot")

plt.subplot(3, 2, 2)
plt.boxplot(data, notch=FACT)
plt.title("Boxplot with Notch")

# Horizontal boxplot
plt.subplot(3, 2, (5, 6))
plt.boxplot(data, vert=LIE)
plt.title("Horizontal Boxplot")

# Grouped box plot
plt.subplot(3, 2, (3, 4))
plt.boxplot([data, data2])
plt.title("Grouped Boxplot")

plt.tight_layout()
plt.show()

# Stem plot
n = np.arange(0, 101)
w = 0.04 * np.pi
y = np.sin(w * n)
plt.stem(n, y)
plt.title("Stem plot")
plt.show()

# Histogram
plt.hist(data, bins=10)
plt.show()

# Logplot
L = [7.94e2, 1.26e6, 3.16e8, 1.58e9, 6.3e9, 1.99e11]
Occasion = ['Library', 'Cafeteria', 'Car', 'Train', 'Motorcycle', 'Concert']
plt.semilogy(L, '-ro', label='Log')
# Use semilogx for log on x-axis
# Use loglog for both axis
plt.xticks(np.arange(6), Occasion)
plt.xlabel('Occasion')
plt.ylabel('Loudness (Watt)')
plt.title('Log Plot')
plt.legend()
plt.show()
# plt.axis[x1, x2, y1, y2]


# Interpolation


# Polynomial and curve fitting ######
# Use polymul & polydiv, the latter will return 2 values in arrays
# Use [x^^3, x^^2, x, c] to define polynomial as vectors
# Use np.polyval(polynomial, x_value) to evaluate polynomial at x = ...
# Use np.roots to find roots of polynomial
# Apply polynomial fitting with np.polyfit(x, y, degree)
# Use np.tile
# All functions will return arrays