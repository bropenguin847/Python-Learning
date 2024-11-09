import numpy as np  # Import NumPy for array operations

# Define the arrays of principal amounts and years
a = np.array([100, 500, 800])
n = np.array([2, 4, 6, 8, 10])
r = 0.09  # Define the interest rate

# Use meshgrid to create 2D arrays for vectorized calculations
N, A = np.meshgrid(n, a)

# Calculate the array B using element-wise operations
B = A * (1 + r) ** N

# Display the arrays A, N, and the resulting array B
print("Array A:")
print(A)
print("\nArray N:")
print(N)
print("\nResult Array B:")
print(B)