"""
Chapter 6 Example 11
"""

import numpy as np
# Saving a NumPy array to a binary file
array = np.array([1, 2, 3])
np.save('array.npy', array)

# Loading a NumPy array from a binary file
loaded_array = np.load('array.npy')
print(loaded_array) # Output: [1 2 3]
