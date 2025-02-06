"""
Chapter 8 Example 1, 2, 3, 4 & 5

Example 1: Exponential plot, uses np.exp
Example 2: Sine wave plt, uses np.sin
Example 3: Sin(ω) graph, uses raw string (r'') originally
Example 4: Plotting polynomials
Example 5: Using subplots
"""

import numpy as np
import matplotlib.pyplot as plt

# Example 1
x1 = np.arange(1, 11)
y1 = np.exp(x1 / 2)
plt.plot(x1, y1)
plt.xlabel('x1')
plt.ylabel('exp(x1/2)')
plt.title('Exp 1: Exponential Plot')
plt.show()


# Example 2
x2 = np.arange(1, 501, 10)
y2 = np.sin(5 * x2) 
plt.plot(x2, y2, '-mo')
# '-mo' represents a magenta line with circle markers plt.xlabel('x2')
plt.ylabel('sin(5x)')
plt.title('Exp 2: Sine Wave Plot')
plt.show()


# Example 3
w = np.linspace(0, 2*np.pi, 1000)
y = np.sin(w)

# fig, ax = plt.subplots()
# ax.plot(w, y)
ticks =       [0, 0.5*np.pi, np.pi, 1.5*np.pi, 2*np.pi]
tick_labels = ['0','0.5π', 'π', '1.5π', '2π']
# ax.set_xticks(ticks)
# ax.set_xticklabels(tick_labels)

plt.plot(w, y, linestyle="--", color="fuchsia", marker="v", label="Data")
plt.xticks(ticks, tick_labels)
plt.xlabel('ω')
plt.ylabel('sin(ω)')
plt.title('Exp 3: Sin(ω) Graph')
plt.grid(True)
plt.legend(loc="upper right")
plt.show()


# Example 4
x = np.arange(-10, 10.5, 0.5)
f_x = 3*x**4 + 2*x**3 + 7*x + 9       # 3x^4 + 2x^3 + 7x + 9
g_x = 5*x**3 + 9*x + 2                # 5x^3 + 9x + 2
plt.plot(x, f_x, '-xm', label='f(x)')
plt.plot(x, g_x, '--ob', label='g(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Exp 4: Polynomial Graph')
plt.legend(loc='lower right')
plt.show()


# Example 5
x5 = np.linspace(0, 10, 100)
y5 = np.cos(3 * x5)
z5 = np.sin(x5)
plt.subplot(2, 1, 1)
plt.title('Exp 5: y = cos(3x)')
plt.plot(x5, y5)

plt.subplot(2, 1, 2)
plt.title('Exp 5: z = sin(x)')
plt.plot(x5, z5)

# Adjusts subplots to avoid overlap
plt.tight_layout()
plt.show()
