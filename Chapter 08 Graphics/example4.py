import numpy as np 
import matplotlib.pyplot as plt 
x = np.arange(-10, 10.5, 0.5) 
f = 3 * x**4 + 2 * x**3 + 7 * x + 9 
g = 5 * x**3 + 9 * x + 2 
plt.plot(x, f, '-xm', label='f(x)') 
plt.plot(x, g, '--ok', label='g(x)') 
plt.legend() 
plt.xlabel('x') 
plt.ylabel('y') 
plt.show()
