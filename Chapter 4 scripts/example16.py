import numpy as np
import time

# Define smaller arrays for testing
a = np.random.randint(1000, size=1000)  # Reduced size for 'a'
n = np.arange(2, 2002, 2)  # Smaller range for 'n' to reduce complexity
r = 0.09

# Measure time for array operation using meshgrid and element-wise operations
start_time = time.time()
N, A = np.meshgrid(n, a)
B = A * (1 + r) ** N
time1 = time.time() - start_time

# Measure time for the nested loop operation
start_time = time.time()
B_loop = np.zeros((len(a), len(n)))  # Initialize B with zeros for loop assignment
for i in range(len(a)):
    for j in range(len(n)):
        B_loop[i, j] = a[i] * (1 + r) ** n[j]
time2 = time.time() - start_time

# Display elapsed times for both methods
print(f"Array Operation Elapsed Time: {time1:.4f} seconds")
print(f"Loop Elapsed Time: {time2:.4f} seconds")
