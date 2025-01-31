"""
Chapter 11 Example 6

Getting general statistics from dataframe
"""

import os
import pandas as pd

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'employees.csv')
# print(os.getcwd())        # Used for troubleshooting
# Load a CSV file
df = pd.read_csv(file_path)

# Display the first 5 rows of the dataset
print(df.head())

# Get the shape of the dataset
print(df.shape)

# Summary statistics of the dataset
print(df.describe())

# Get mean, median and std from dataframe
print(df['Salary'].mean())
print(df['Bonus %'].median())
print(df['Bonus %'].std())
