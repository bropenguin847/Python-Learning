import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(1.2, 0.2, 30)
plt.figure()

plt.boxplot(data, widths=0.5)
numDataPoints = len(data)
x = np.ones(numDataPoints)
x_jittered = x + 0.2 * np.random.randn(numDataPoints)
plt.scatter(x_jittered, data, marker='.',
edgecolor='b', facecolor='b', linewidth=1)
plt.title('Scatter Box Plot')
plt.xlabel('Data')
plt.ylabel('The weight (in kg) of 30 fruits')
plt.show()