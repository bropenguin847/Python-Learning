"""
Practice for question 2 in finals

Q2: Chapter 5-6 (Libraries: Numpy & Pandas)
    Theory questions and write Python script for:
        - Creating and calling a function
        - Prompt input and output
        - Import/export data from/to external file
"""


import pickle
import numpy as np
import pandas as pd

mat1 = np.matrix([[1, 2], [3, 4]])
mat2 = np.matrix([[5, 6], [7, 8]])

# Creating functions
# The def keyword is used to define a function in Python
def matrix_add(a, b):
    """
    Input (matrix): a & b
    Output: a + b
    """
    return a + b

# Using built-in functions
num_list = [1, 2, 3, 4, 5, 6, 7]
length = len(num_list)
print(length)

# Calling a function
result = matrix_add(mat1, mat2)
print(result)


# Prompt input from user
user_int = int(input('Put a number here: '))
user_float = float(input('Enter a floating number: '))
print(f'The user has entered int: {user_int}, while the floating num is: {user_float}')

# Using arrays
# Loading a NumPy array from a binary file, saved from Q1
loaded_array = np.load('array_save.npy')
print(loaded_array) # Output: [1 2 3]

# Import and export data
with open('example.txt', 'w') as file:
    file.write('Practice Question for Q2:\n')
    file.write(str(loaded_array))

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)


# Using pickle
# Saving an object to a binary file
family = {'Rick': 'Gramps', 'Morty': 'Grandson', 'Summer': 'Rebel', 'Jerry': 'Loser'}

with open('data.pkl', 'wb') as file:
    pickle.dump(family, file)

# Loading an object from a binary file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
print(f'The loaded data in pickle file are\n{loaded_data}')
