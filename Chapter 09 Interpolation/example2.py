""" Chapter 9 Example 2
"""

import numpy as np
import matplotlib.pyplot as plt


def api_interpolation(km):
    """Function to calculate API values using interpolation"""

    # Given data points
    distances = np.array([0, 6, 15, 23, 30])  # Kilometres
    api_values = np.array([100, 180, 199, 280, 310])  # API values

    # Generate distances from 0 to 30 km at every 1 km
    full_distances = np.arange(0, 31, 1)

    # Interpolating API values linearly between the known points
    interpolated_api = np.interp(full_distances, distances, api_values)

    # Use np.atleast_1d to convert any input to a 1D array
    km = np.atleast_1d(km)

    # Extract API values for the requested km points
    result = {}
    for k in km.astype(int):  # Ensure indices are integers
        result[k] = round(interpolated_api[k], 2)
        print(f"API value at km {k} is {result[k]}")
    print("\n")
    
    # Plotting the data
    plt.figure()
    plt.plot(distances, api_values, 'o', label='Given API values')  # Known data points
    plt.plot(full_distances, interpolated_api, 'x:',
             label='Interpolated API values')  # Interpolated values
    plt.xlabel('Distance (km)')
    plt.ylabel('API Value')
    plt.title('API Calculation from 5 Stations')
    plt.grid(True)
    plt.xticks(distances, ['Kulai', 'Senai', 'Skudai', 'Perling', 'Johor Bahru'], rotation=45)
    plt.legend()
    plt.show()

    return result

# Example usage: Finding API values at specified km points
api_interpolation(10)          # Single integer
api_interpolation([3, 8, 11, 26])  # List of km points
api_interpolation(np.linspace(0, 30, 5))  # Linspace for evenly spaced km points
