"""
A sorting algorithm that channels the spirit of Stalin with Soviet Era's Iron Fist approach.
The elements that are not in order are ruthlessly removed from the list, and sent to
the Gulag far far away
"""

import numpy as np

def stalin_sort(array):
    """
    Takes in an array, and returns sorted array
    """
    array = array.tolist()  # Convert numpy array to Python list
    sorted_array = [array[0]]       # The first array always makes the cut :)
    for i in range(1, len(array)):
        if array[i] >= sorted_array[-1]:
            sorted_array.append(array[i])
    return sorted_array

# Creates an array with size 20, filled with numbers from 0 - 100
arr_1d = np.random.randint(100, size=20)
print(f'This is the original array:\n{arr_1d}')
result = stalin_sort(arr_1d)
print(f'Gulag survivors:\n{result}')
