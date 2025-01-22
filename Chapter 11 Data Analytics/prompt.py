"""
Process and analyze temperature data over time.

This script:
1. Loads temperature data (`ydata`) from a CSV file.
2. Reads the sampling interval (`daypersample`) from a text file.
3. Generates an array of time values (`xdata`) based on the sampling interval.
4. Calls the `datastat` function to analyze and plot the data.

Libraries:
- numpy
- pandas
- datastat_module (contains the `datastat` function)
"""

import numpy as np
import pandas as pd
from datastat_module import datastat

# Load ydata from the CSV file
ydata = pd.read_csv('dataTemp1.csv').values

# Load daypersample from the text file
# Encoding specifies the file encoding ('utf-8' for text files).
with open('daypersample.txt', 'r', encoding='utf-8') as file:
    daypersample = float(file.read().strip())

# Generate xdata (equivalent to MATLAB's 1:daypersample:length(temp(:,1)))
xdata = np.arange(1, len(ydata[:, 0]) * daypersample + 1, daypersample)

# Call the datastat function
datastat(xdata, ydata, 'Days', 'Temperature', 'PLOT')
