"""
Set 2 
A retail chain tracks the monthly profits (in $1000s) of 4 branches over a year, stored in a 
CSV file named profits.xlsx: 

1.  Write a Python script to load the data from profits.xlsx and perform polynomial
    curve fitting for Branch_Z using polynomial orders 1, 3, and 4.
2.  Using the fitted models, predict the profits for Branch_Z for the next three months 
    (January, February, and March of the following year). 
3.  Create a user interface for the users to select which order they want to display in the
    graph. Example; order 1 or order 2 or order 3 or order 1,2 and 3.
4.  Plot the original data and overlay the polynomial fitting curves on the same graph
    based on user selection.

Using the best-fit polynomial model from above, calculate the expected profits for Branch_Z 
for the first, second, and third months of the following year. 
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'profits.xlsx')
df = pd.read_excel(file_path, sheet_name='Monayyyy')
print(df)
