import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 11, 1)  
y1 = 3 * t + 2  
y2 = 2 * t**2 + 1 
 
plt.plot(y1,t,y2,t)
plt.xlabel('Plant')
plt.ylabel('Days')
plt.title('Plant growth over the days')
plt.legend(["Plant A","Plant B"])
plt.show()

