import pandas as pd

# Load a CSV file
df = pd.read_csv('employees.csv')

# Display the first 5 rows of the dataset
print(df.head())

# Get the shape of the dataset
print(df.shape)

# Summary statistics of the dataset
print(df.describe())
