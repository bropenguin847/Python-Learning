import numpy as np 
import matplotlib.pyplot as plt 

# Generate random data
data = np.random.randn(100, 3) 

# Create a figure for the plot
plt.figure()

# Plot a basic box plot
plt.boxplot(data)

# Add a title
plt.title('Basic Box Plot')

# Display the plot
plt.show()
