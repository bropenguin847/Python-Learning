""" 
This is an example code in Python, which contains snippet of code from all the chapters.
Documentation string will be on top of the code, providing a summary
This is what a typical Python code will look like.

Author: Keith L
"""

import os
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d, PchipInterpolator

# Get user input for radius
radius = float(input('Enter the radius of the circle: '))

# Calculate the area of the circle
area = math.pi * radius * radius

# Print the calculated area
print('The area of the circle with radius', radius, 'is:', area)

# Get user input for two numbers
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

# Calculate the sum of the two numbers
sum_of_numbers = num1 + num2

# Print the sum
print(f'The sum of {num1} and {num2} is: {sum_of_numbers}')




# Chapter 4: Control Flow (Python)
def calculate_tax(income):
    """Calculates income tax based on different income brackets."""
    tax1 = (0.1 * income) * (income <= 10000)
    tax2 = (1000 + 0.2 * (income - 10000)) * (income > 10000 and income <= 20000)
    tax3 = (3000 + 0.5 * (income - 20000)) * (income > 20000)
    return tax1 + tax2 + tax3

def capacitor_charge(V, R, C, time_limit):
    """Simulates capacitor charging in an RC circuit."""
    t = 0
    q = 0
    Q = []
    T = []
    time_increment = 0.5
    while q <= time_limit:
        q = C * V * (1 - math.exp(-t / (R * C)))
        Q.append(round(q, 4))
        T.append(t)
        t += time_increment
    return Q, T

# Chapter 5: Functions (Python)
def calculate_circuit_parameters(a, b):
    """Performs basic arithmetic operations on circuit parameters."""
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else None
    return addition, subtraction, multiplication, division

# Chapter 6: Input and Output Data (Python)
def myMesh(V, R):
    """Calculates mesh circuit currents."""
    def separateIR(R):
        """Separates resistances and current indicators."""
        r = R[0, :]
        i = R[1:, :].astype(bool)
        totalLoop = R.shape - 1
        return i, r, totalLoop
    i, r, M = separateIR(R)
    Rmat = np.zeros((M, M))
    for m in range(M):
        for n in range(M):
            indI = np.logical_and(i[m, :], i[n, :])
            if n != m:
                Rmat[m, n] = -np.sum(r[indI])
            else:
                Rmat[m, n] = np.sum(r[indI])
    I = np.linalg.solve(Rmat, V)
    return I

def analyze_circuit_data(file_path):
    """Analyzes circuit data from an Excel spreadsheet."""
    df = pd.read_excel(file_path, sheet_name='Sheet1')
    I1_list = []
    I2_list = []
    data = df.to_numpy()
    for row in data:
        try:
            R1, R2, R3 = row[1:4]
            V1, V2 = row[4:6]
            R = np.array([
                [R1, R2, R3],
                [1, 1],
                [1, 1]
            ])
            V = np.array([V1, V2])
            I = myMesh(V, R)
            I1_list.append(I)
            I2_list.append(I[1])
        except Exception as e:
            print(f"An error occurred while processing row {row}: {e}")
    I_values_df = pd.DataFrame({'I1': I1_list, 'I2': I2_list})
    with pd.ExcelWriter(file_path, mode='a', if_sheet_exists='overlay') as writer:
        I_values_df.to_excel(writer, startcol=6, startrow=1, index=False, header=False)

# Chapter 8: Graphics (Python)
def plot_rc_circuit_response(R, C, f_start, f_end, num_points):
    """Plots magnitude and phase response of an RC circuit."""
    f = np.linspace(f_start, f_end, num_points)
    H = 1 / (1 + 1j * 2 * np.pi * f * R * C)
    Magnitude = np.abs(H)
    Phase = np.angle(H)
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(f / 1000, Magnitude)
    plt.xlabel('Frequency (kHz)')
    plt.ylabel('Magnitude')
    plt.xticks(np.arange(f_start / 1000, (f_end / 1000) + 1, step=2))
    plt.subplot(2, 1, 2)
    plt.plot(f / 1000, Phase / np.pi)
    plt.xlabel('Frequency (kHz)')
    plt.ylabel('Phase (π rad)')
    plt.yticks(np.arange(-1, 1.5, 0.5), [f'{tick:.1f}π' for tick in np.arange(-1, 1.5, 0.5)])
    plt.tight_layout()
    plt.show()

def plot_bode_plot(R, C, f_start, f_end, num_points):
    """Generates a Bode plot for an RC circuit."""
    f = np.linspace(f_start, f_end, num_points)
    H = 1 / (1 + 1j * 2 * np.pi * f * R * C)
    Magnitude = 20 * np.log10(np.abs(H))
    Phase = np.angle(H)
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.semilogx(f, Magnitude)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.title('Magnitude vs Frequency (Log Scale)')
    plt.subplot(2, 1, 2)
    plt.semilogx(f, Phase / np.pi)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phase (π radians)')
    plt.yticks(np.arange(-1, 1.5, 0.5), [f'{tick:.1f}π' for tick in np.arange(-1, 1.5, 0.5)])
    plt.tight_layout()
    plt.show()

def create_histogram(data, num_bins):
    """Creates a histogram to visualize data distribution."""
    plt.figure()
    plt.hist(data, bins=num_bins)
    plt.xlabel('Data Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()

# Chapter 9: Data Interpolation (Python)
def api_interpolation(km):
    """Calculates API values at given km points using linear interpolation."""
    km = np.atleast_1d(km)
    distances = np.array([2-5])
    api_values = np.array([6])
    interpolated_api = interp1d(distances, api_values, kind='linear')
    full_distances = np.arange(0, 31)
    result = {}
    for k in km.astype(int):
        result[k] = round(interpolated_api(k), 2)
        print(f"API value at km {k} is {result[k]}")
    plt.figure()
    plt.plot(distances, api_values, 'o', label='Given API values')
    plt.plot(full_distances, interpolated_api(
        full_distances), 'x:', label='Interpolated API values')
    plt.xlabel('Distance (km)')
    plt.ylabel('API Value')
    plt.title('API Calculation from 5 Stations')
    plt.grid(True)
    plt.xticks(distances, ['Kulai', 'Senai', 'Skudai', 'Perling', 'Johor \nBahru'],
               rotation=45)
    plt.legend()
    plt.show()
    return result

def vle_diagram(x_values, y_values, x_interp):
    """Plots a VLE diagram with spline and PCHIP interpolation."""
    spline_interpolation = interp1d(x_values, y_values, kind='cubic')
    pchip_interpolation = PchipInterpolator(x_values, y_values)
    y_spline = spline_interpolation(x_interp)
    y_pchip = pchip_interpolation(x_interp)
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, 'o', label='Data Points')
    plt.plot(x_values, spline_interpolation(x_values),
             '--', label='Spline Interpolation')
    plt.plot(x_values, pchip_interpolation(x_values),
             '-.', label='PCHIP Interpolation')
    plt.scatter(x_interp, y_spline, color='red',
                zorder=5, label=f'Spline y({x_interp})={y_spline:.2f}')
    plt.scatter(x_interp, y_pchip, color='green',
                zorder=5, label=f'PCHIP y({x_interp})={y_pchip:.2f}')
    plt.xlabel('Liquid Mole Fraction, x')
    plt.ylabel('Vapor Mole Fraction, y')
    plt.title('VLE Diagram for Benzene-Toluene at 1 atm')
    plt.legend()
    plt.grid(True)
    plt.show()
    print(f"Spline interpolation: y({x_interp}) = {y_spline:.5f}")
    print(f"PCHIP interpolation: y({x_interp}) = {y_pchip:.5f}")


def main():
    """Main function to demonstrate combined code functionalities."""
    # Chapter 4 Examples
    income = 15000
    tax = calculate_tax(income)
    print(f"Tax for income {income} is: {tax}")

    Q, T = capacitor_charge(V=9, R=4, C=1, time_limit=2)
    print("Capacitor Charge (Q):", Q)
    print("Time (T):", T)

    # Chapter 5 Examples
    param1 = 10
    param2 = 5
    add, sub, mul, div = calculate_circuit_parameters(param1, param2)
    print("Addition:", add)
    print("Subtraction:", sub)
    print("Multiplication:", mul)
    print("Division:", div)

    # Chapter 6 Examples
    current_dir = os.path.dirname(__file__)
    circuit_data_file = os.path.join(current_dir, 'circuit_analysis.xlsx')
    analyze_circuit_data(circuit_data_file)

    # Chapter 8 Examples
    plot_rc_circuit_response(R=4.7e3, C=0.47e-6, f_start=0, f_end=10000, num_points=10000)
    plot_bode_plot(R=4.7e3, C=0.47e-6, f_start=1, f_end=10000, num_points=10000)

    data = np.random.randn(1000)
    create_histogram(data, num_bins=50)

    # Chapter 9 Examples
    api_interpolation([7, 8])

    x_values = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    y_values = np.array([0.00, 0.21, 0.38, 0.51, 0.62, 0.71, 0.79, 0.86, 0.91, 0.96, 1.0])
    vle_diagram(x_values, y_values, x_interp=0.45)


if __name__ == "__main__":
    main()