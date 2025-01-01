"""
Contains multiple exercises from Chapter 5, such as
creating functions, multiple inputs and outputs, importing function
"""
import numpy as np
from exercise5 import celsius_to_fahrenheit

# Exercise 1: Create simple function
def square(num):
    '''
    Squares a given numer
    '''
    return num ** 2
print(square(9))    # Output: 81

# Exercise 2: Multiple Inputs and Outputs
def calculate(a, b):
    '''
    Calculates sum, subtract, product and quotient of 2 numbers
    '''
    total = a + b
    subtract = a - b
    product = a * b
    quotient = a / b if b != 0 else 'Undefined'
    return total, subtract, product, quotient
print(calculate(5, 6))    # Output: (11, -1, 30, 0.8333333333333334)

# Exercise 3: Import Function
# By saving this .py file in the same folder/directory, we can include this file
# into another .py file, thus importing the function
# There are two types:  and Import entire module
#   - Import functions only:    from chapter5_practice import calculate
#   - Import entire module:     import chapter5_practice

# Exercise 4: Defining and calling a function

# Define function
def broadcast_multiply(a, b):
    '''Takes 2 array, and performs broadcasting on them before multiplying'''
    return a * b

# Defining the arrays
a = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
# Define a 2D array with shape (3, 1)
b = np.array([[1], [2], [3]])
result = broadcast_multiply(a, b)
print("Result of a * b:")
print(result)

# Exercise 5: Converting a script into a function-based script in Python
# Create a python file (exercise5.py), define a function called celsius_to_fahrenheit
#   that takes a Celsius array as input and returns the converted Fahrenheit values.
# Use formula F = C  9 / 5 + 32
# From exercise5.py, import celsius_to_fahrenheit. Then, pass an array of
#   Celsius temperatures to get the Fahrenheit conversion

# use_exercise5.py, importing function placed at top of code
# Define each row of the 2D array using np.linspace
row1 = np.linspace(-20, 0, 3) # 3 values from -20 to 0
row2 = np.linspace(20, 50, 3) # 3 values from 20 to 50
row3 = np.linspace(60, 100, 3) # 3 values from 60 to 100
# Combine rows to form a 2D array
celsius_2d_array = np.array([row1, row2, row3])
# Convert the 2D array to Fahrenheit
fahrenheit_2d_array = celsius_to_fahrenheit(celsius_2d_array)
# Print the results
print("Celsius temperatures (2D array):")
print(celsius_2d_array)
print("\nFahrenheit temperatures (2D array):")
print(fahrenheit_2d_array)

