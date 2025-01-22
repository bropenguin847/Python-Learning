"""
Practice for question 1 in finals

Q1: Chapter 1-4 (Libraries: Numpy)
    - Flowchart to pseudocode OR Pseudocode to flowchart conversion
    - Create and access array, subscripting, reshape
    - Understand and write script for condition
    - while loop and for loop
"""


import numpy as np

# 1D array
arr1d = np.array([6, 6, 6])
# 2D array
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])
# 3D array
arr3d = np.array([[[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]],
                   [[11, 22, 33],
                    [44, 55, 66],
                    [77, 88, 99]]])

print(arr1d)
print(type(arr3d))
