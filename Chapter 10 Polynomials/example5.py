"""
Chapter 10 Example 5
This example demonstrates the use of numpy.polyval(),
which can evaulate a poly when x = ...
"""

import numpy as np

# Coefficients of the polynomial P(x) = 2x^2 + 4x + 1
coefficients = [2, 4, 1]

# Evaluate the polynomial at x = 3
x_value = 3
result = np.polyval(coefficients, x_value)

# Output the result
print('P(x) = 2x^2 + 4x + 1')
print("P(3) =", result)  # P(3) = 31
