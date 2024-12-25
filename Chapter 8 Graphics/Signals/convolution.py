import matplotlib.pyplot as plt
import numpy as np

class waveform:
    def __init__(self, time, t1, t2):
        self.time = time
        self.t1, self.t2 = t1, t2
        self.center = (t2-t1)/2
t = np.linspace(-2, 3, 1000)

def graphlabel(title, xlabel, ylabel):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)

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
fig1c = x1 + x2

yt = np.convolve(x1, x2, mode='full')
t_conv = np.linspace(triangle.time[0] + square.time[0], triangle.time[-1] + square.time[-1], len(yt))
#############
plt.subplot(3,2,1)
plt.plot(t, x1, color='mediumblue')
graphlabel('Figure 1 (a)', 'Time (seconds)', 'Triangle, x1')
plt.axis([-2, 3, 0, 2])

plt.subplot(322)
plt.plot(t, x2, 'firebrick')
graphlabel('Figure 1 (b)', 'Time (seconds)', 'Rectangle, x2')
plt.axis([-2, 3, 0, 2])

plt.subplot(3, 2, 3)
plt.plot(t, x2, 'crimson', t, x1, 'navy')
graphlabel('Overlap', 'Time (seconds)', '')
plt.axis([-2, 3, 0, 2])

plt.subplot(3, 2, 4)
plt.plot(t, fig1c, 'deepskyblue')
graphlabel('Figure 1 (c)', 'Time (seconds)', 'z')
plt.axis([-2, 3, 0, 4])

plt.subplot(3,2,(5,6))
plt.plot(t_conv, yt, color='forestgreen')
graphlabel('Figure 1 (d)', 'Time (seconds)', 'Convolution, y')
plt.axis([-3, 6, 0, 500])

plt.tight_layout()
plt.show()

#################################################
# Task 2
slant = waveform(t, -1, 1)
g = np.zeros_like(t)
h = np.zeros_like(t)

for i, time in enumerate(slant.time):
    if slant.t1 <= time <= slant.t2:
        g[i] = 1 * (time +1)
    else:
        g[i] = 0
      
# Define square
square1 = waveform(t, -1, 0)
square2 = waveform(t, 1, 2)

for i, time in enumerate(t):
    if square1.t1 <= time <= square1.t2:
        h[i] = 2
        
    if square2.t1 <= time <= square2.t2:
        h[i] = 1

# yt = gt + ht
fig2c= g + h
        
yt = np.convolve(g, h, mode='full')
#t_conv = np.linspace(square1.time[0] + slant.time[0], square2.time[-1] + slant.time[-1], len(yt))
t_conv = np.linspace(-4,4, len(yt))
###################
plt.subplot(2,2,1)
plt.plot(t, g, color='midnightblue')
graphlabel('Figure 2 (a)', 'Time (seconds)', 'Triangle, g')
plt.axis([-2, 3, 0, 3])

plt.subplot(222)
plt.plot(t, h, color='dodgerblue')
graphlabel('Figure 2 (b)', 'Time (seconds)', 'Rectangle, h')
plt.axis([-2, 3, 0, 3])

plt.subplot(223)
plt.plot(t, fig2c, color='cornflowerblue')
graphlabel('Figure 2 (c)', 'Time (seconds)', 'z')
plt.axis([-2, 3, 0, 3])

plt.subplot(224)
plt.plot(t_conv, yt, color='mediumseagreen')
graphlabel('Figure 2 (d)', 'Time (seconds)', 'Convolution, y')
plt.axis([-3, 4, 0, 1000])

plt.tight_layout()
plt.show()