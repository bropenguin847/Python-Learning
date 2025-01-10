"""
Example 3: USER DEFINED FUNCTION

How to Write a Function using def:
▪ Define the function: Use the def keyword followed by the
function name and parentheses ().
▪ Add Parameters (optional): List any input parameters inside the
parentheses.
▪ Add a Colon : ndicate the start of the function body.
▪ Write the Function Body: Indent the code inside the function.
▪ Return (optional): Use return to send back a result from the
function.
"""

# Defining a simple function
def greet(name):
    """prints out name, 'name' is the parameter"""
    print(f"Hello, {name}!") # Function body with an indented block

# Calling the function
greet("Alice") # Output: Hello, Alice!

def square(number):
    """ function that takes one input and returns one output."""
    return number ** 2
print(square(4)) # Output: 16

def analyze_number(num):
    """
    function that takes one input and returns multiple outputs.
    Returns Boolean of is_even and integer of square
    """
    is_even = num % 2 == 0
    square = num ** 2
    return is_even, square
even, sq = analyze_number(5)
print('Is Even:', even, 'Square:', sq)
# Output: Is Even: False Square: 25

def add(a, b):
    """function that takes multiple inputs and returns one output."""
    return a + b
print(add(3, 7)) # Output: 10

def calculate(a, b):
    """function that takes multiple inputs and returns multiple outputs."""
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else None
    return addition, subtraction, multiplication, division
add_result, sub_result, mul_result, div_result = calculate(8, 2)
print("Addition:", add_result, "Subtraction:", sub_result,
"Multiplication:", mul_result, "Division:", div_result)
# Output: Addition: 10 Subtraction: 6 Multiplication: 16 Division: 4.0

def hello_world():
    """
    Function with no input and no output. Performs a task but does not take any inputs and
    does not return any values.
    """
    print("Hello, World!") # Prints a message to the console

# Calling the function
hello_world() # Output: Hello, World!

import math
def calculate_circle_area(radius):
    """
    Add Help Documentation in Python
    Use help(function_name) or function_name.__doc__ to view the documentation.

    Calculate the area of a circle given its radius.
    Parameters: radius (float): The radius of the circle.
    Returns:
    float: The area of the circle.
    """
    return math.pi * radius ** 2

# Accessing help
help(calculate_circle_area)
