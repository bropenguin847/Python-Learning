import matplotlib.pyplot as plt
import numpy as np

class waveform:
    def __init__(self, time, t1, t2):
        self.time = time
        self.t1, self.t2 = t1, t2
        self.center = (t2-t1)/2
t = np.linspace(-2, 3, 1000)

# Task 1
# Define triangle
triangle = waveform(t, 0, 2)
x1 = np.zeros_like(triangle.time)      # Initialize with zero first

for i, time in enumerate(triangle.time):
    # Rising part
    if triangle.t1 <= time <= triangle.center:
        x1[i] = 2 * time
    # Falling part
    elif triangle.center < time <= triangle.t2:
        x1[i] = 2 * (2 - time)

# Define square
square = waveform(t, -1, 1)
x2 = np.zeros_like(square.time)

for i, time in enumerate(square.time):
    x2[i] = 0
    if square.t1 <= time <= square.t2:
        x2[i] = 1

# z(t) = x1(t) + x2(t)
fig3 = x1 + x2

yt = np.convolve(x1, x2, mode='full')
t_conv = np.linspace(triangle.time[0] + square.time[0], triangle.time[-1] + square.time[-1], len(yt))
#################################################
plt.subplot(3,2,1)
plt.plot(t, x1, '-b')
plt.title('Figure 1 (a)') 
plt.xlabel('Time (seconds)') 
plt.ylabel('Triangle, x1')
plt.grid(True)
plt.axis([-2, 3, 0, 2])

plt.subplot(322)
plt.plot(t, x2, 'r')
plt.title('Figure 2 (b)') 
plt.xlabel('Time (seconds)')
plt.ylabel('Rectangle, x2')
plt.grid(True)
plt.axis([-2, 3, 0, 2])

plt.subplot(3, 2, 3)
plt.plot(t, x2, '-r', t, x1, 'b')
plt.grid(True)
plt.axis([-2, 3, 0, 2])

plt.subplot(3, 2, 4)
plt.plot(t, fig3, 'm')
plt.title('Figure 3 (c)') 
plt.xlabel('Time (seconds)')
plt.ylabel('z')
plt.axis([-2, 3, 0, 4])
plt.grid(True)

plt.subplot(3,2,(5,6))
plt.plot(t_conv, yt, color='green')
plt.title('Figure 4 (d)')
plt.xlabel('Time (seconds)')
plt.ylabel('Convolution, y')
plt.grid(True)
plt.axis([-3, 6, 0, 500])

plt.tight_layout()
plt.show()


# Task 2
slant = waveform(t, -1, 1)
g = np.zeros_like(t)
h = np.zeros_like(t)

for i, time in enumerate(slant.time):
    if slant.t1 <= time <= slant.t2:
        g[i] = 1 * (time +1)
    else:
        g[i] = 0

plt.plot(t, g)
plt.title('Figure 2 (a)')
plt.xlabel('Time (seconds)')
plt.ylabel('Triangle, g')
plt.grid(True)
plt.axis([-2, 2, 0, 3])
plt.show()