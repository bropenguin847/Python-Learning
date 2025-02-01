"""
Chapter 10 Example 7
roots are all values that will return f(x) = 0
"""

import numpy as np

# Define the polynomial coefficients
# f(x) = x^3 + x^2 - 4x - 4
coefficients = [1, 1, -4, -4]

# Find the roots using numpy.roots()
roots = np.roots(coefficients)

# Output the roots
print("Roots of the polynomial are:", roots)
