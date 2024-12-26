import os
import time

from IPython import get_ipython

# Send the %clear command to the console
get_ipython().run_line_magic('clear', '')

time.sleep(0.3)

import numpy as np

# Define arrays of diameters and heights for 5 different cones
D = np.array([3, 5, 7, 9, 11])  # Example diameters
H = np.array([4, 6, 8, 10, 12])  # Example heights

# Calculate the volumes using vectorized operations
V = (1/12) * np.pi * D**2 * H

# Display the calculated volumes
print("Volumes of cones using vectorization:")
print(np.round(V, 4))  # Rounded to four decimal places
