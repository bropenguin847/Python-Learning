""" This is an example code in Python
Insert documentation string here
Most of the time, this is what a typical Python code will look like
"""

# Import library at the top of code
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100, 3)
plt.figure()
plt.boxplot(data)
plt.title('Basic Box Plot')
plt.show()

