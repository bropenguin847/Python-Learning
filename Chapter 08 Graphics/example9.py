import numpy as np 
import matplotlib.pyplot as plt 

L = [7.94e2, 1.26e6, 3.16e8, 1.58e9, 6.3e9, 1.99e11]
Occasion = ['Library', 'Cafeteria', 'Car', 'Train', 'Motorcycle', 'Concert']

plt.subplot(2, 1, 1)
plt.plot(L, '-bo')
plt.xticks(np.arange(6), Occasion)
plt.xlabel('Occasion')
plt.ylabel('Loudness (Watt)')
plt.title('Normal Plot')

plt.subplot(2, 1, 2)
plt.semilogy(L, '-bo')
plt.xticks(np.arange(6), Occasion)
plt.xlabel('Occasion')
plt.ylabel('Loudness (Watt)')
plt.title('Log Plot')

plt.tight_layout()
plt.show()
