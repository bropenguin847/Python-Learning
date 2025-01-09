import numpy as np 
import matplotlib.pyplot as plt 

data = np.random.randn(100, 3) 

plt.figure() 
plt.boxplot(data, notch=True, vert=False) 
plt.title('Horizontal Box Plot with Notch')
plt.show()
