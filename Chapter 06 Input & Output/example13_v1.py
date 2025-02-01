"""
Chapter 6 Example 12 version 1
"""

import pandas as pd
import numpy as np
import os
from myMesh import myMesh  # Import the myMesh function from myMesh.py

# Get the current script directory
current_dir = os.path.dirname(__file__)
# Ensure the Excel file is in the same directory
file_path = os.path.join(current_dir, 'circuit_analysis.xlsx')

# Load the Excel file
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Initialize lists to store the computed currents
I1_list = []
I2_list = []

# Convert DataFrame to NumPy array for easier iteration
data = df.to_numpy()

# Iterate over each row in the NumPy array to compute currents
for row in data:
    try:
        # Extract R1, R2, R3 and V1, V2 values
        R1, R2, R3 = row[1:4]  # R1, R2, R3 are in columns B, C, D
        V1, V2 = row[4:6]      # V1, V2 are in columns E, F

        # Prepare the R matrix
        R = np.array([
            [R1, R2, R3],
            [1, 0, 1],  # Assuming similar indicator for current flows in all sets
            [0, 1, 1]
        ])

        # Prepare the voltage vector
        V = np.array([V1, V2])

        # Compute currents using myMesh function
        I = myMesh(V, R)

        # Append the computed currents to the lists
        I1_list.append(I[0])
        I2_list.append(I[1])

    except Exception as e:
        print(f"An error occurred while processing row {row}: {e}")

# Create a DataFrame with only I1 and I2 to append to the original file
I_values_df = pd.DataFrame({'I1': I1_list, 'I2': I2_list})

# Load the existing sheet, keeping the other data intact and appending I1 and I2 correctly
with pd.ExcelWriter(file_path, mode='a', if_sheet_exists='overlay') as writer:
    I_values_df.to_excel(writer, startcol=6, startrow=1, index=False, header=False)  
# Adjusted startrow to 1

# Display confirmation message
print("I1 and I2 have been successfully appended to the Excel file starting from the correct row.")