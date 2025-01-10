"""
Chapter 6 Example 12
"""

import os
import pandas as pd
import openpyxl

# Set the file path relative to the current script directory
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'tempData.xlsx')

# Read the relevant data from the Excel file
# Adjusts automatically to existing data
tempC = pd.read_excel(file_path, sheet_name='Sheet1', header=None).iloc[1, 1:]

# Convert Celsius to Fahrenheit
tempF = tempC * 9/5 + 32
 
# Display results
print("Celsius to Fahrenheit Conversion:")
for c, f in zip(tempC, tempF):
    print(f'{c:.0f}°C {f:10.2f}°F')

# Load the existing workbook to prevent overwriting the entire file
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
    # Write the Fahrenheit data to a specific range without erasing existing content
    output_data = pd.DataFrame([tempF])
    output_data.to_excel(writer, sheet_name='Sheet1',
                         startcol=1, startrow=2, index=False, header=False)
