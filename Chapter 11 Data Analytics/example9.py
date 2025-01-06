"""
Detecting outlier using IQR. IQR stands for interquartile range.
"""

import pandas as pd
# Use IQR to detect outlier

# Create the DataFrame
data = {
    'Fruit': ['Orange', 'Watermelon', 'Pear', 'Apple', 'Banana', 'Grapes', 'Mango'],
    'Quantity': [10, 12, 100, 23, 18, 20, 2]
}
df = pd.DataFrame(data)

# Calculate the Interquartile Range (IQR)
Q1 = df['Quantity'].quantile(0.25)
Q3 = df['Quantity'].quantile(0.75)
IQR = Q3 - Q1

# Define outlier boundaries
lower_bound = Q1 -1.5 * IQR
upper_bound = Q3 +1.5 * IQR

# Detect outliers
df['Outlier'] = (df['Quantity'] < lower_bound) | (df['Quantity'] > upper_bound)

# Display the DataFrame with the outlier column
print("DataFrame with Outlier Column:")
print(df)
