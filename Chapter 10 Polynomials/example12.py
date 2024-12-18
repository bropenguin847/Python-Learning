import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from Excel, skipping the first row
file_path = 'waterusage.xlsx'  # Ensure the file path is correct
df = pd.read_excel(file_path, usecols='B:C', skiprows=1)

# Extract day and water usage data
day, water = df.iloc[:, 0].values, df.iloc[:, 1].values

# Define the number of polynomial degrees to fit
N = 5
waterFit = [np.polyval(np.polyfit(day, water, n), day) for n in range(1, N + 1)]  # Fit and evaluate in one line
labels = ['Measured Data'] + [f'Polynomial Order = {n}' for n in range(1, N + 1)]


# Calculate and print R-squared values
R2 = [1 - np.sum((fit - water) ** 2) / np.sum((water - np.mean(water)) ** 2) for fit in waterFit]
print("R-SQUARED VALUES:")
for n, r2 in enumerate(R2, 1):
    print(f'Polynomial Order {n} = {r2:.4f}')

# Plot original data and fitted curves
plt.plot(day, water, 'x', label='Measured Data')
for fit, label in zip(waterFit, labels[1:]):
    plt.plot(day, fit, label=label)

plt.xlabel('Day')
plt.ylabel('Water Usage (Litre)')
plt.title('Water Usage for 1 Harvesting Cycle')
plt.legend(fontsize=8)  # Set legend font size to 8
plt.grid(True)
plt.show()


# Get and print coefficients for the 3rd-order polynomial
coeffs_order_3 = np.polyfit(day, water, 3)
print(f"Coefficients for 3rd-order polynomial: {coeffs_order_3}")
