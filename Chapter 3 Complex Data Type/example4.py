import numpy as np

# Define an array (2x2)
A = np.array([[1, 2],
              [3, 4]])

print("Array A:")
print(A)

# Shape of the array (rows, columns)
array_shape = A.shape
print("\nShape of the array (rows, columns):")
print(array_shape)  # (2, 2)

# Total number of elements in the array
array_size = A.size
print("\nTotal number of elements in the array:")
print(array_size)  # 4

# Number of dimensions of the array
array_ndim = A.ndim
print("\nNumber of dimensions of the array:")
print(array_ndim)  # 2

# Size of each dimension
rows = len(A)       # Number of rows
columns = len(A[0]) # Number of columns
print("\nSize of each dimension:")
print(f"Rows: {rows}, Columns: {columns}")
