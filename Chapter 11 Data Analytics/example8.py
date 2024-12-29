import pandas as pd

# Create a sample DataFrame with missing values
data = {
    'Fruit': ['Orange', 'Watermelon', 'Pear', 'Apple', None, 'Grapes'],
    'Quantity': [10, None, 16, 23, 18, 20],
    'Price': [2.5, 3.0, None, 2.8, 3.2, 2.9]
}

df = pd.DataFrame(data)

# Check for missing values using isnull()
missing_values = df.isnull()

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Display the logical array (True = missing, False = not missing)
print("\nLogical array indicating missing values")
print('(True = missing, False = not missing)')
print(missing_values)

# Count the missing values in each column
missing_count = df.isnull().sum()
print("\nCount of missing values in each column:")
print(missing_count)
