import numpy as np  # Import NumPy for array operations

# Define the array of principal amounts and the interest rate
a = np.array([100, 500, 800])
r = 0.09

# Create an empty array to store the results
B = np.zeros((3, 5))  # 3 rows for a, 5 columns for n values

# Loop through the values of n (2, 4, 6, 8, 10)
for idx, n in enumerate(range(2, 12, 2)):
    B[:, idx] = a * (1 + r) ** n  # Calculate and store the results

# Display the results matrix
print(B)
######################################
#   using while loop
a = np.array([100, 500, 800])
r = 0.09
B = np.zeros((3, 5))  # 3 rows for a, 5 columns for n values

idx = 0
n = 2
while n <= 10:  #using while loop
    B[:, idx] = a * (1 + r) ** n
    idx += 1
    n += 2
print(B)