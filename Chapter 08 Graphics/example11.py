"""
Chapter 8 Example 11
Histogram plot
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)

# plt.figure()
plt.hist(data, bins=50)
plt.xlabel('Data Value')
plt.ylabel('Frequency')
plt.title('Histogram as part of EDA')
plt.show()
