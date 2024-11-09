import numpy as np

# Step 1: Assign values to variables
g = 9.81  # acceleration due to gravity

# Vectorize t for time intervals
t = np.arange(0, 6)  # Creates an array [0, 1, 2, 3, 4, 5]

# Step 2: Calculate the displacement s using the formula
s = g * t**2 / 2  # Performs element-wise squaring and multiplication

# Display the results
print("Elapsed time (t):", t)         # Shows time intervals
print("Displacement (s):", np.round(s, 4))  # Displays the calculated displacements
