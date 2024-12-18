import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from Excel file
df = pd.read_excel('sensor_calibration.xlsx')  # Replace with your file path if needed

# Extract the data for voltage (V) and temperature (T)
V = df['V'].values
T = df['T'].values

# Apply polynomial fitting (degree 1, linear fit)
p = np.polyfit(V, T, 1)

# Evaluate the polynomial at the voltage points
sT = np.polyval(p, V)

# Print the polynomial equation
print(f'T(V) = {p[0]:.2f}V + {p[1]:.2f}')

# Plot the data and the fitted curve
plt.scatter(V, T, label='Collected Data', color='blue', marker='x')
plt.plot(V, sT, label='Fitted Polynomial Curve', color='red')
plt.title('Sensor Calibration')
plt.xlabel('Sensor Reading (V)')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()
