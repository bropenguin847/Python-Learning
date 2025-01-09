import numpy as np 
import matplotlib.pyplot as plt 

# Generate random data
data = np.random.randn(100, 3) 

# Create a figure for the plot
plt.figure()

# Plot a box plot with notches
plt.boxplot(data, notch=True)

# Add a title
plt.title('Notch Box Plot')

# Display the plot
plt.show()
