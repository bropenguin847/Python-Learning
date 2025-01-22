"""
Chapter 4 Example 15
Using meshgrid
"""

import numpy as np

# Define the arrays of principal amounts and years
a = np.array([100, 500, 800])
n = np.array([2, 4, 6, 8, 10])
r = 0.09  # Define the interest rate

# Use meshgrid to create 2D arrays for vectorized calculations
N, A = np.meshgrid(n, a)

# Calculate the array B using element-wise operations
B = A * (1 + r) ** N

# Display the arrays A, N, and the resulting array B
print(f"Array A:\n{A}")
print(f"\nArray N:\n{N}")
print(f"\nResult Array B:\n{B}")
