import numpy as np

# Define two 2x2 arrays
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Array A:")
print(A)

print("\nArray B:")
print(B)

# 1. Element-wise Addition
element_wise_add = A + B
print("\nElement-wise Addition (A + B):")
print(element_wise_add)

# 2. Element-wise Subtraction
element_wise_sub = A - B
print("\nElement-wise Subtraction (A - B):")
print(element_wise_sub)

# 3. Element-wise Multiplication
element_wise_mul = A * B
print("\nElement-wise Multiplication (A * B):")
print(element_wise_mul)

# 4. Element-wise Right Division
element_wise_right_div = A / B
print("\nElement-wise Right Division (A / B):")
print(element_wise_right_div)

# 5. Element-wise Left Division
element_wise_left_div = B / A
print("\nElement-wise Left Division (B / A):")
print(element_wise_left_div)

# 6. Element-wise Power
element_wise_power = A ** 2
print("\nElement-wise Power (A ** 2):")
print(element_wise_power)
