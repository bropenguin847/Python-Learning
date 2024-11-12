import numpy as np

A = np.matrix([[1, 2],
              [3, 4]])

B = np.matrix([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# 1. Matrix Addition
matrix_add_result = A + B
print("\nMatrix Addition (A + B):")
print(matrix_add_result)

# 2. Matrix Subtraction
matrix_sub_result = A - B
print("\nMatrix Subtraction (A - B):")
print(matrix_sub_result)

# 3. Matrix Multiplication  Using @ operator
matrix_mul_result = A @ B
print("\nMatrix Multiplication (A @ B):")
print(matrix_mul_result)

# Alternatively, using np.matmul()
matrix_mul_result_alt = np.matmul(A, B)
print("\nMatrix Multiplication (np.matmul(A, B)):")
print(matrix_mul_result_alt)

# 4. Matrix Left Division
# Solving AX = B using np.linalg.solve
# Interpreted as B \ A or X = A.T*B
matrix_left_div_result = np.linalg.solve(A, B)
print("\nMatrix Left Division (np.linalg.solve(A, B)):")
print(matrix_left_div_result)

# 5. Matrix Right Division
# Solving XA = B using np.linalg.solve
# Interpreted as A / B or X = B*A.T
matrix_right_div_result = np.linalg.solve(B.T, A.T).T
print("\nMatrix Right Division (np.linalg.solve(B.T, A.T).T):")
print(matrix_right_div_result)

# 6. Matrix Power
# Using np.linalg.matrix_power() to raise matrix A to the power of 2
matrix_power_result = np.linalg.matrix_power(A, 2)
print("\nMatrix Power (np.linalg.matrix_power(A, 2)):")
print(matrix_power_result)

# 7. Matrix Transpose
transpose_result = A.T
print("\nMatrix Transpose (A.T):")
print(transpose_result)