import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# 1. Demonstrate Precedence of Transpose vs Multiplication
# Transpose happens before multiplication
precedence_result_1 = A.T @ B
print("\nPrecedence 1 (Transpose before Multiply - A.T @ B):")
print(precedence_result_1)

# 2. Demonstrate Precedence of Parentheses
# Parentheses change the order of operations
precedence_result_2 = (A + B) @ B
print("\nPrecedence 2 (Parentheses first - (A + B) @ B):")
print(precedence_result_2)

# 3. Demonstrate Power Precedence
# Power operation happens before multiplication
precedence_result_3 = np.linalg.matrix_power(A, 2) @ B
print("\nPrecedence 3 (Power before Multiply - np.linalg.matrix_power(A, 2) @ B):")
print(precedence_result_3)

# 4. Demonstrate Multiplication and Division Precedence
# Multiplication happens before solving division operations
precedence_result_4 = np.linalg.solve(B.T, (A @ B).T).T
print("\nPrecedence 4 (Multiply before Divide - np.linalg.solve(B.T, (A @ B).T).T):")
print(precedence_result_4)

# 5. Demonstrate Precedence of Addition and Multiplication
# Multiplication happens before addition
precedence_result_5 = A @ B + B
print("\nPrecedence 5 (Multiply before Addition - A @ B + B):")
print(precedence_result_5)

# 6. Combining Multiple Precedence
# Complex combination to demonstrate full precedence
precedence_result_6 = (np.linalg.matrix_power(A, 2) + A.T) @ np.linalg.solve(B, A)
print("\nPrecedence 6 (Combination of Power, Transpose, Addition, and Division):")
print(precedence_result_6)
