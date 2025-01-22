"""
Chapter 3 Example 9
Perform element wise operation on array
"""

import numpy as np

# Define arrays A and B
A = np.array([0, 0, 1, 1])
B = np.array([0, 1, 0, 1])

# Element-wise operations
and_result = A & B
or_result = A | B
not_result = ~A
not_result2 = ~B

print("Element-wise AND (A & B):", and_result)  # Output: [0 0 0 1]
print("Element-wise OR (A | B):", or_result)    # Output: [0 1 1 1]
print("Element-wise NOT (~A):", not_result)     # Output: [1 1 0 0] -> [-1 -1 -2 -2]
print("Element-wise NOT (~B):", not_result2)     # Output: [-1 -2 -1 -2]
