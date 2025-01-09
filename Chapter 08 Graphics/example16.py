import numpy as np 
import matplotlib.pyplot as plt 

data = np.random.randn(100) 
plt.figure() 
plt.boxplot(data, widths=0.5)

numDataPoints = len(data) 
x = np.ones(numDataPoints) 
x_jittered = x + 0.2 * np.random.randn(numDataPoints)

plt.scatter(x_jittered, data, marker='.', edgecolor='b', facecolor='b', linewidth=1)
plt.title('Scatter Box Plot')
plt.xlabel('Data')
plt.ylabel('Values')

plt.show()
