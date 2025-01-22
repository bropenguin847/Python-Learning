"""
Chapter 3 Example 5
Vectors
"""

import numpy as np

# Define interest rate and number of years
r = 0.09
n = 10

# Single invested value
A1 = 100
# Calculate final balance for the single value
B1 = A1 * (1 + r) ** n
print("Single value calculation:")
print(f"B1 = {B1:.4f}")  # Output: 236.7364

# Vectorized invested values
A2 = np.array([100, 200, 500, 1000, 4000])
# Calculate final balances for each value in the array
B2 = A2 * (1 + r) ** n
print("\nVectorized calculation with multiple values:")
print("B2 =", np.round(B2, 4))  # Output: [236.7, 473.5, 1183.7, 2367.4, 9469.5]
