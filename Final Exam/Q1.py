"""
Practice for question 1 in finals

Q1: Chapter 1-4 (Libraries: Numpy)
    - Flowchart to pseudocode OR Pseudocode to flowchart conversion
    - Create and access array, subscripting, reshape
    - Understand and write script for condition
    - while loop and for loop
"""


import random
import numpy as np

# Creating array
# 1D array
arr1d = np.array([69, 420, 1984, 1234, 5678])
# 2D array
arr2d = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15]])
# 3D array
arr3d = np.array([[[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]],
                   [[11, 22, 33],
                    [44, 55, 66],
                    [77, 88, 99]],
                    [[111, 121, 131],
                     [212, 222, 232],
                     [313, 323, 333]]])

# Subscripting array using colon :
extract1 = arr1d[1:4]           # Column 2-4
extract2 = arr2d[1, 0:2]        # Row 2, column 1-2
extract3 = arr3d[1, 0:2, 1:]    # 2nd page, row 1-2, column 2-3

# Fancy indexing
arr1 = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
arr2= np.array([arr1, 2*arr1])
X = arr1[[1, 2, 0]]
Y = arr2[[1, 1, 0]]    # There is difference between double bracket and single bracket
Z = arr2[1, 1, 0]      # For single bracket it is just basic indexing, fancy indexing uses double bracket.  

print(arr2)
print(Y)
print(Z)

# Check array shape and attributes
arr_shape = arr3d.shape
arr_size = arr3d.size       # Returns number of elements
arr_ndim = arr3d.ndim
arr_rows = len(arr2d)
arr_columns = len(arr2d[0])

# Reshaping, using Transpose, meshgrid and broadcasting
print(arr2d.T)


# if, elif, else statements
num = random.randint(1, 100)
print(f'The random number is {num}')

if num < 20:
    print('The number is unremarkable')
elif 30 < num < 65:
    print('The number is average')
elif 70 < num < 80:
    print('The number is in a sweet spot')
else:
    print('The number means nothing')

# To be used in Q2
# Saving a NumPy array to a binary file
array_save = arr3d
np.save('array_save.npy', array_save)
