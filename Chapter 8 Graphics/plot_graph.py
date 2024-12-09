# Draw a triangle and a hexagon using matplotlib. The hexagon shape must be in magenta color
# and triangle line in blue color

import matplotlib.pyplot as plt
import numpy as np

# Triangle coordinates
# xt = [-1, 0, 1, -1]
# yt = [-0.5, 0.5, -0.5, -0.5]
# plt.plot(xt, yt, 'b:D')

# # Hexagon coordinates
# xh = [-1, -2, -1, 1, 2, 1, -1]
# yh = [-1, 0, 1, 1, 0, -1, -1]
# plt.plot(xh, yh, "m--s")
# plt.show()

# Draw a parallelogram and Triangle
# xp = [0, 1, 5, 4, 0]
# yp = [1, 4, 4, 1, 1]
# plt.plot(xp, yp, "-rs")
# xt = [1, 4, 1, 1]
# yt = [2, 2.5, 3, 2]
# plt.plot(xt, yt, ":bo")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.title("Parallegram and Triangle")
# plt.show()

# xcos = np.linspace(0, 10, 200)
# ycos = np.cos(np.pi * xcos)
# plt.subplot(2, 1, 1)
# plt.plot(xcos, ycos, "-b")
# plt.title("y = cos(pi x)")
# plt.tight_layout()

# xsin = np.arange(0, 10.1, 0.1)
# ysin = np.sin(0.3 * np.pi * xsin)
# plt.subplot(2, 1, 2)
# plt.plot(xsin, ysin, "-k")
# plt.title(f"y = sin(3/10 $\pi$ x)")

# x = np.linspace(0, 1, 100)

# for F in range(1, 11):
#     hz = F * 100
#     y = np.sin(2 * np.pi * F * x)
#     plt.subplot(5, 5, F)
#     plt.plot(x, y, F)
#     plt.xlabel("Time, t (s)")
#     plt.ylabel("lalalla")
#     plt.title(f"Frequency {F} Hz")
# x = np.linspace(-4, 4, 100)
# y1 = np.cos(x)
# y2 = 1 - (x**2/2) + (x**4/24)
# plt.subplot(221)
# plt.plot(x, y1, "-bo")
# plt.subplot(222)
# plt.plot(x, y2, "-ko")
# plt.subplot(212)
# plt.plot(x, y1, "-bo", x, y2, "-ko")




# Try out the star question
# Rotate the star around 4 points
# Perhaps can show animation
plt.tight_layout()
plt.show()