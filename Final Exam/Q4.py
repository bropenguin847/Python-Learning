"""
Practice for question 4 in finals

Q4: Chapter 11 (Libraries: Numpy, Matplotlib & Pandas)
    Theory questions and write Python script for:
        - Creating dataframe
        - Missing data handling, remove and fill data
        - Outliers handling using IQR

        - Sorting arrays
"""


import os
import numpy as np
import pandas as pd
import matplotlib as plt

# Creating easy dataframe
# Define the variables (fruits and quantities)
Fruit = ['Orange', 'Watermelon', 'Pear', 'Apple', 'Banana', 'Grapes', 'Mango', 
         'Pineapple', 'Strawberry', 'Blueberry', 'Kiwi', 'Papaya']
Quantity = [10, 12, 16, 23, 18, 20, 25, 30, 8, 14, 5, 11]

# Create the DataFrame
df_easy = pd.DataFrame({'Fruit': Fruit, 'Quantity': Quantity})


# Read from csv file and creating dataframe
currrent_dir = os.path.dirname(__file__)
file_path = os.path.join(currrent_dir, "random_data.csv")
# df = pd.read_excel(file_path, sheet_name = 'xxx')
df = pd.read_csv(file_path)

# print('The full dataframe\n', df)
print('The shape of dataframe\n', df.shape)
print('The first 5 rows of dataframe\n', df.head())
print('Statistics of dataframe\n', df.describe())
print('Mean of age\n', df['Age'].mean())
print('Median of Height\n', df['Height'].median())
print('Std of Bank Acc\n', df['Bank Acc'].std())

# Missing data handling, remove and fill data
# bank_acc has missing values
bank_acc = np.array(df['Bank Acc'].values)
df_range = df.shape[0]
# Interpolate for x-points
x_points = np.arange(df_range)

valid = ~np.isnan(bank_acc)     # Returns a Boolean array
missing = np.isnan(bank_acc)
bank_acc[missing] = np.interp(x_points[missing], x_points[valid], bank_acc[valid])
df['Bank Acc'] = bank_acc.round(2)

# Outliers handling using IQR
# Finding out the height outliers
Q1 = df['Height'].quantile(0.25)
Q3 = df['Height'].quantile(0.75)
IQR = Q3 - Q1

# Define outlier boundaries with 1.5 being the standard, the value can be tweaked
# Boundaries can be 2.0 or 1.75
lower_bound = Q1 -1.5 * IQR
upper_bound = Q3 +1.5 * IQR

# Marking outlier in new seperate column
df['Outlier Height'] = (df['Height'] < lower_bound) | (df['Height'] > upper_bound)
print(df.head())


# Sorting arrays
# Sorting a 1D Array, default is ascending
arr1d = np.array([6, 3, 7, 29, 8, 11, 171, 39, 92])
result = np.sort(arr1d)
print("\nSorted 1D Array:", result)

# Sorting 1D array descending
result2 = np.sort(arr1d)[::-1]
print("\nDescending 1D Array:", result2)

# Sorting a 2D Array by Columns
X = np.array([[3, 5, 2],
              [6, 2, 7],
              [2, 4, 5]])
sort_col = np.sort(X, axis=0)
print("\nSorted 2D Array by Columns (ascending):\n", sort_col)

# Sorting a 2D Array by Rows
sort_row = np.sort(X, axis=1)
print("\nSorted 2D Array by Rows (ascending):\n", sort_row)

# Sorting a 2D Array in Descending Order by Rows
row_des = np.sort(X, axis=1)[:, ::-1]
print("\nSorted 2D Array by Rows (descending):\n", row_des)

# Sorting a 2D Array in Ascending Order by Columns (default behaviour)
col_ascen = np.sort(X, axis=0)
print("\nSorted 2D Array by Columns (ascending - default):\n", col_ascen)

# Sorting a 2D Array in Descending Order by Columns
col_descn = np.sort(X, axis=0)[::-1]
print("\nSorted 2D Array by Columns (descending):\n", col_descn)
