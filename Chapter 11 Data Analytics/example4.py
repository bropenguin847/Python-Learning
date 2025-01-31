"""
Chapter 11 Example 4

Sorting Arrays
"""

import numpy as np

# Example 1: Sorting a 1D Array
x = np.array([6, 3, 7, 2, 8])
y = np.sort(x)
print("Sorted 1D Array:", y)

# Example 2: Sorting a 2D Array by Columns
X = np.array([[3, 5, 2], [6, 2, 7]])
Ycol = np.sort(X, axis=0)
print("\nSorted 2D Array by Columns (ascending):\n", Ycol)

# Example 3: Sorting a 2D Array by Rows
Yrow = np.sort(X, axis=1)
print("\nSorted 2D Array by Rows (ascending):\n", Yrow)

# Example 4: Sorting a 2D Array in Ascending Order by Columns (default behaviour)
Ycolasc = np.sort(X, axis=0)
print("\nSorted 2D Array by Columns (ascending - default):\n", Ycolasc)

# Example 5: Sorting a 2D Array in Descending Order by Columns
Ycoldes = np.sort(X, axis=0)[::-1]
print("\nSorted 2D Array by Columns (descending):\n", Ycoldes)

# Example 6: Sorting a 2D Array in Descending Order by Rows
Yrowdes = np.sort(X, axis=1)[:, ::-1]
print("\nSorted 2D Array by Rows (descending):\n", Yrowdes)
