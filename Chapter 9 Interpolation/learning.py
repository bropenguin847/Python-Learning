import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# y = np.array([0,1,1,0])
# n1 = np.arange(0, 4)
# n2 = np.arange(0, 3.2, 0.2)

# xnearest = interpld(n1, y, kind = 'nearest')
# xlinear = interpld(n1, y, kind = 'linear')
# xspline = interpld(n1, y, kind = 'cubic')

# xnearest_val = xnearest(n2)
# xlinear_val = xlinear(n2)
# xspline_val = xspline(n2)

# yval = np.array([0, 4, 14, 20])
# xval = np.array([0, 2, 6, 8])
# x_new = np.arange(2, 8.5, 0.5)
# xspline = interp1d(xval, yval, kind='cubic')

# ynearest = xspline(10)
# print(xspline(10))

# speed = np.array([20, 50, 100, 140])
# fuel = np.array([13, 15, 18, 11])
# question = [25, 62, 90]

# xlinear = interp1d(speed, fuel, kind='linear')
# # print(xlinear(question))
# for i in question:
#     fuel_comp = xlinear(i)
#     print(f'Fuel comp: {i}km/h is {fuel_comp:.2f} km/L')

# speed_new = np.arange(20, 142, 2)
# yaxis = xlinear(speed_new)

# plt.plot(speed_new, yaxis, ':sr', label='Extrapolated')
# plt.plot(speed, fuel, 'o', label= 'Original')
# plt.xlabel('Speed (km/h)')
# plt.ylabel('Fuel Consumption (km/L)')
# plt.legend()
# plt.show()

diameter = np.array([12, 20, 25, 40, 50, 65, 75, 100])
flow = np.array([2.1, 8.2, 14.7, 50.6, 90.9, 181, 264, 563])
plt.plot(diameter, flow, '-o', label = 'Original')

new_diameter = np.arange(12, 101)

ylinear = interp1d(diameter, flow, kind='linear')
graph_linear = ylinear(new_diameter)
plt.plot(new_diameter, graph_linear, '-m', label = 'Linear')

ynearest = interp1d(diameter, flow, kind='nearest')
graph_nearest = ynearest(new_diameter)
plt.plot(new_diameter, graph_nearest, ':g', label = 'Nearest')


ycubic = interp1d(diameter, flow, kind='cubic')
graph_spline = ycubic(new_diameter)
plt.plot(new_diameter, graph_nearest, ':r', label = 'Cubic')

plt.legend()
plt.show()