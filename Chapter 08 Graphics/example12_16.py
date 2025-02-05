"""
Chapter 8 Example 12, 13, 14, 15 & 16
Example 12: Boxplot
Example 13: Boxplot with notch
Example 14: Group boxplot
Example 15: Horizontal boxplot
Example 16: Scatter box plot
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate random data for Example 12 & 13
data = np.random.randn(100, 3)

# Example 12: Boxplot
# Create a figure for the plot
plt.figure()

# Plot a basic box plot
plt.boxplot(data)
plt.title('Basic Box Plot')
plt.show()


# Example 13: Boxplot with notch
# Create a figure for the plot
plt.figure()
# Plot a box plot with notches
plt.boxplot(data, notch=True)

plt.title('Notch Box Plot')
plt.show()


# Example 14: Grouped box plot
# Generate random data for two groups
group1 = np.random.randn(100)
group2 = np.random.randn(100) + 2

plt.boxplot([group1, group2])
plt.title('Grouped Box Plot')
plt.show()


# Example 15: Horizontal boxplot
hdata = np.random.randn(100, 3)
# plt.figure()
plt.boxplot(hdata, notch=True, vert=False)
plt.title('Horizontal Box Plot with Notch')
plt.show()


# Example 16: Scatter box plot
sdata = np.random.randn(100)
plt.figure()
plt.boxplot(sdata, widths=0.5)

data_points = len(sdata)
x = np.ones(data_points)
x_jitter = x + 0.2 * np.random.randn(data_points)

plt.scatter(x_jitter, sdata, marker='.', edgecolor='b', facecolor='b', linewidth=1)
plt.title('Scatter Box Plot')
plt.xlabel('Data')
plt.ylabel('Values')
plt.show()
