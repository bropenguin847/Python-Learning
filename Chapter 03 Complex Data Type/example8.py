import numpy as np

# Define a 2x2 array with complex numbers
a = np.array([[1 + 1j, 2 + 2j], 
              [3 + 3j, 4 + 4j]])

print("Array a:") ; print(a)

# Conjugate transpose of the array (changes the sign of imaginary parts and transposes)
conjugate_transpose = a.conj().T
print("\nConjugate Transpose of a (a.conj().T):")
print(conjugate_transpose)

# Pure transpose of the array (transposes without changing imaginary parts)
pure_transpose = a.T
print("\nPure Transpose of a (a.T):")
print(pure_transpose)
