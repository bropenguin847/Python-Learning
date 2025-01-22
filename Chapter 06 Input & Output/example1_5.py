"""
Chapter 6 Example 1, 2, 3, 4, 5
Getting input from user and formatting output strings
"""

# Example 1
# Request user input for height and width as numbers
height = float(input('Enter height: '))
width = float(input('Enter width: '))

# Calculate the area
area = 0.5 * width * height
print(f'Area = {area}')

# Example 2-4, can access x directly with interactive window
x = 10
print(x)
print(f'The value of x is {x}') # Outputs: The value of x is 10

# Example 5
cows = 5    # Define the variable 
# Formatted output using f-strings 
print(f'There are {cows:7.2f} cows in the pasture')
