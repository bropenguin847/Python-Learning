import numpy as np  # Import NumPy for array operations

# Define the array of income values
inc = np.array([4000, 12000, 18000, 23000, 30000])

# Calculate the tax components without loops or decision statements
tax1 = (0.1 * inc) * (inc <= 10000)
tax2 = (1000 + 0.2 * (inc - 10000)) * (inc > 10000) * (inc <= 20000)
tax3 = (3000 + 0.5 * (inc - 20000)) * (inc > 20000)

# Sum the tax components to get the total tax for each income
tax = tax1 + tax2 + tax3

# Display the income and corresponding tax values
print(f"Income: {inc}")
print(f"Tax:    {tax}")
