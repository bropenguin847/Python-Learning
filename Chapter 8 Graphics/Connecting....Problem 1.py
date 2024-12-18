import matplotlib.pyplot as plt
import numpy as np

# Problem 1
t = np.arange(0, 11, 1)
a = 2  
v = a * t  

plt.plot(t, v)
plt.xlabel('Time(t)')
plt.ylabel('Velocity(v)')
plt.title('Problem 1')
plt.show()


