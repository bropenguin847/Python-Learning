"""
Set 1 
The annual rainfall data (in millimeters) for 6 regions is recorded monthly and stored in a 
excel file named rainfall_data.xlsx: 

1.  Write a Python script to load the data from rainfall_data.xlsx and perform
    polynomial curve fitting for Region_C using polynomial orders 2, 3, and 4.
2.  Using the fitted models, predict the rainfall for Region_C for the next three months
    (January, February, and March of the following year).
3.  Create a user interface for the users to select which order they want to display in the
    graph. Example; order 1 or order 2 or order 3 or order 1,2 and 3.
4.  Plot the original data and overlay the polynomial fitting curves on the same graph
    based on user selection.

Using the best-fit polynomial model from above, compute the expected rainfall for Region_C 
for the first, second, and third months of the following year. Print the results in a tabular 
format.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'rainfall_data.xlsx')
df = pd.read_excel(file_path, sheet_name='RainOnMeBaby')
print(df)
