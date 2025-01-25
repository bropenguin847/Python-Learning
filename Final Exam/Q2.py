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
import pickle

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
user_int = int(input('Put a number here: '))
user_float = float(input('Enter a floating number: '))
print(f'The number user has entered is: {user_int}, while the floating num is: {user_float}')

# Using arrays
# Loading a NumPy array from a binary file, saved from Q1
loaded_array = np.load('array_save.npy')
print(loaded_array) # Output: [1 2 3]

# Import and export data
with open('example.txt', 'w') as file:
    file.write('Practice Question for Q2: ')
    file.write(str(loaded_array))

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
