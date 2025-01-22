"""
Practice for question 2 in finals

Q2: Chapter 5-6 (Libraries: Numpy & Pandas)
    Theory questions and write Python script for:
        - Creating and calling a function
        - Prompt input and output
        - import/export data from/to external file
"""


import numpy as np
import pandas as pd

mat1 = np.matrix([[1, 2], [3, 4]])
mat2 = np.matrix([[5, 6], [7, 8]])

# Creating functions
def matrix_add(a, b):
    """
    Input (matrix): a & b
    Output: a + b
    """
    return a + b

# Calling a function
result = matrix_add(mat1, mat2)
print(result)

# Prompt input from user
user = int(input('Put a number here: '))
print(f'The number user has entered is: {user}')
