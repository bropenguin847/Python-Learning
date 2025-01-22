"""
Chapter 3 Example 8
Conjugate and Transpose on arrays (with complex numbers)
"""

import numpy as np

# Define 2x2 array with complex numbers
A = np.array([[1 + 1j, 2 + 2j],
              [3 + 3j, 4 + 4j]])

print("Array A:")
print(A)

# Conjugate the array (change sign of imaginary parts only)
conjugate = A.conj()
print("\nConjugate of A (A.conj()) : ")
print(conjugate)

# Conjugate transpose of the array (changes the sign of imaginary parts and transposes)
conjugate_transpose = A.conj().T
print("\nConjugate Transpose of A (A.conj().T) : ")
print(conjugate_transpose)

# Pure transpose of the array (transposes without changing imaginary parts)
pure_transpose = A.T
print("\nPure Transpose of A (A.T):")
print(pure_transpose)
