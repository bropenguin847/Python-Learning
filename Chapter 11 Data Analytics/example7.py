"""
Chapter 11 Example 7

Creating dataframe
"""

import pandas as pd

# Define the variables (fruits and quantities)
Fruit = ['Orange', 'Watermelon', 'Pear', 'Apple', 'Banana', 'Grapes', 'Mango', 
         'Pineapple', 'Strawberry', 'Blueberry', 'Kiwi', 'Papaya']
Quantity = [10, 12, 16, 23, 18, 20, 25, 30, 8, 14, 5, 11]

# Create the DataFrame
df = pd.DataFrame({'Fruit': Fruit, 'Quantity': Quantity})

# Display the DataFrame
print(df)

# Calculate and display the mean of the Quantity column
mean_quantity = df['Quantity'].mean()
print("Mean of Quantity:", mean_quantity)
