import numpy as np 
import matplotlib.pyplot as plt 
x = np.linspace(0, 10, 100) 
y = np.cos(3 * x) 
z = np.sin(x) 
plt.subplot(2, 1, 1) 
plt.plot(x, y) 
plt.title('y = cos(3x)') 
plt.subplot(2, 1, 2) 
plt.plot(x, z) 
plt.title('z = sin(x)') 
plt.tight_layout() 
# Adjusts subplots to avoid overlap 
plt.show() 
