import matplotlib.pyplot as plt
import numpy as np

class Waveform:
    '''
    t1 = start
    t2 = end
    center = t1 - t2, center point
    '''
    def __init__(self, time, t1, t2):
        self.time = time
        self.t1, self.t2 = t1, t2
        self.center = (t2-t1)/2
t = np.linspace(-2, 3, 500)

def graph_label(title, xlabel, ylabel):
    '''quick code to plot figure'''
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)

# Task 1
# Define triangle & rectangle
triangle = Waveform(t, 0, 2)
x1 = np.zeros_like(t)      # Initialize with zero first
square = Waveform(t, -1, 1)
x2 = np.zeros_like(t)

for i, time in enumerate(t):
    # Rising part
    if triangle.t1 <= time <= triangle.center:
        x1[i] = 2 * time
    # Falling part
    elif triangle.center < time <= triangle.t2:
        x1[i] = 2 * (2 - time)

for i, time in enumerate(t):
    x2[i] = 0
    if square.t1 <= time <= square.t2:
        x2[i] = 1

# z(t) = x1(t) + x2(t)
z = x1 + x2
# y(t) = x1(t) * x2(t)
y = np.convolve(x1, x2, mode='full') / 100    # Adjust for sampling rate by dividing 100
t_conv = np.linspace(triangle.time[0] + square.time[0], triangle.time[-1] + square.time[-1], len(y))

plt.subplot(3,2,1)
plt.plot(t, x1, 'mediumblue')
graph_label('Figure 1 (a)', 'Time (seconds)', 'Triangle, x1')
plt.axis([-2, 3, 0, 3])

plt.subplot(322)
plt.plot(t, x2, 'firebrick')
graph_label('Figure 1 (b)', 'Time (seconds)', 'Rectangle, x2')
plt.axis([-2, 3, 0, 3])

plt.subplot(3, 2, 3)
plt.plot(t, z, 'deepskyblue')
graph_label('Figure 1 (c)', 'Time (seconds)', 'z')
plt.axis([-2, 3, 0, 3])

plt.subplot(3,2,4)
plt.plot(t_conv, y, 'forestgreen')
graph_label('Figure 1 (d)', 'Time (seconds)', 'Convolution, y')
plt.axis([-2, 6, 0, 3])

plt.tight_layout()
plt.show()

#####################################################
# Task 2
slant = Waveform(t, -1, 1)
g = np.zeros_like(t)
h = np.zeros_like(t)

# Define slant
for i, time in enumerate(slant.time):
    if slant.t1 <= time <= slant.t2:
        g[i] = 1 * (time +1)
    else:
        g[i] = 0

# Define square
square1 = Waveform(t, -1, 0)
square2 = Waveform(t, 1, 2)

for i, time in enumerate(t):
    if square1.t1 <= time <= square1.t2:
        h[i] = 2
    if square2.t1 <= time <= square2.t2:
        h[i] = 1

# z(t) = g(t) + h(t)
z = g + h
# yt = g(t) * h(t)
y = np.convolve(g, h, mode='full') / 100    # Adjust for sampling rate by dividing 100
t_conv = np.linspace(square1.time[0] + slant.time[0], square2.time[-1] + slant.time[-1], len(y))

plt.subplot(2,2,1)
plt.plot(t, g, 'blueviolet')
graph_label('Figure 2 (a)', 'Time (seconds)', 'Triangle, g')
plt.axis([-2, 3, 0, 3])

plt.subplot(222)
plt.plot(t, h, 'mediumvioletred')
graph_label('Figure 2 (b)', 'Time (seconds)', 'Rectangle, h')
plt.axis([-2, 3, 0, 3])

plt.subplot(223)
plt.plot(t, z, 'cornflowerblue')
graph_label('Figure 2 (c)', 'Time (seconds)', 'z')
plt.axis([-2, 3, 0, 3])

plt.subplot(224)
plt.plot(t_conv, y, 'mediumseagreen')
graph_label('Figure 2 (d)', 'Time (seconds)', 'Convolution, y')
plt.axis([-4, 4, 0, 3])

plt.tight_layout()
plt.show()
