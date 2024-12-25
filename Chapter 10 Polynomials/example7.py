import numpy as np

# Define the polynomial coefficients for f(x) = x^3 + x^2 - 4x - 4
coefficients = [1, 1, -4, -4]

# Find the roots using numpy.roots()
roots = np.roots(coefficients)

# Output the roots
print("Roots of the polynomial are:", roots)