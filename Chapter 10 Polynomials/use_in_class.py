import numpy as np
import matplotlib.pyplot as plt

# measured_current = np.array([20,    16,  12,   8,  4,   0, -4,  -8, -12, -16, -20])
# sensor =           np.array([10.4,8.16,5.65,4.89,2.36,-0.2,-1,-3.6,-4.6,-8.1,-9.6])

# fitted = np.polyfit(measured_current, sensor, 1)
# fitted_sensor = np.polyval(fitted, measured_current)

# plt.plot(measured_current, fitted_sensor, label='Curve Fitted Data', color='red')
# plt.scatter(measured_current, sensor, label = 'Measured Data', color = 'blue', marker='x')
# plt.title('Current Sensor Calibration')
# plt.xlabel('Measured Current (A)')
# plt.ylabel('Sensor Reading (V)')
# plt.legend()
# plt.grid(True)
# plt.show()

pipe_diameter = np.array([12, 20, 25, 40, 50, 65, 75, 100])
flow_rate = np.array([2.1, 8.2, 14.7, 50.6, 90.9, 181, 264, 563])
diameter_new = np.arange(0, 155, 5)

fit_linear = np.polyfit(pipe_diameter, flow_rate, 1)
new_linear = np.polyval(fit_linear, diameter_new)

fit_quad = np.polyfit(pipe_diameter, flow_rate, 2)
new_quad = np.polyval(fit_quad, diameter_new)

fit_cubic = np.polyfit(pipe_diameter, flow_rate, 3)
new_cubic = np.polyval(fit_cubic, diameter_new)

fit_quart = np.polyfit(pipe_diameter, flow_rate, 4)
new_quart = np.polyval(fit_quart, diameter_new)

plt.plot(pipe_diameter, flow_rate, 'bo', label='Data')
plt.plot(diameter_new, new_linear, '-r', label='Linear Fit')
plt.plot(diameter_new, new_quad, '-.y', label='Quadratic Fit')
plt.plot(diameter_new, new_cubic, '--m', label='Cubic Fit')
plt.plot(diameter_new, new_quart, ':g', label='Quartic Fit')
plt.title('Fit of Water flow')
plt.xlabel('Measured Current (A)')
plt.ylabel('Sensor Reading (V)')
plt.legend()
plt.grid(True)
plt.show()