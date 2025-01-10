"""
Example 2: Library functions
Functions available through importing Python libraries
    Examples: Functions from numpy, pandas, etc.
"""

# 1. math.sqrt() - Computes the square root of a number
import math
result = math.sqrt(16) # Output: 4.0
print("Square Root:", result)

# 2. numpy.array() - Creates a numpy array
import numpy as np
array = np.array([1, 2, 3]) # Creates a numpy array
print("Numpy Array:", array)

# 3. pandas.Series() - Creates a pandas Series
import pandas as pd
series = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print("Pandas Series:\n", series)

# 4. random.choice() - Selects a random element from a list
import random
choices = ['apple', 'banana', 'cherry']
random_choice = random.choice(choices) # Randomly selects one item from the list
print("Random Choice:", random_choice)
