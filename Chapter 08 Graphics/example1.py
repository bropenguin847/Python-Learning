import numpy as np 
import matplotlib.pyplot as plt 
x = np.arange(1, 11) 
y = np.exp(x / 2) 
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('exp(x/2)')
plt.title('Exponential Plot')
plt.show()
