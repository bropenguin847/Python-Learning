import numpy as np

# Temperature values for 9 consecutive days
x = np.array([19, 20, 18, 17, 20, 23, 25, 24, 23])

# Sort and find indices for the 2 highest and 2 lowest temperatures
sorted_x_desc = np.sort(x)[::-1]  # Sort in descending order
sorted_x_asc = np.sort(x)         # Sort in ascending order

# Highest 2 values and their respective days
highest_values = sorted_x_desc[:2]
highest_indices = np.argsort(x)[::-1][:2] + 1  # Days are indices + 1

# Lowest 2 values and their respective days
lowest_values = sorted_x_asc[:2]
lowest_indices = np.argsort(x)[:2] + 1  # Days are indices + 1

# Printing formatted output
print("Highest 2")
print(f"{'no.':<5} {'Temp':<5} {'Day':<5}")
for i, (temp, day) in enumerate(zip(highest_values, highest_indices), start=1):
    print(f"{i:<5} {temp:<5} {day:<5}")

print("Lowest 2")
print(f"{'no.':<5} {'Temp':<5} {'Day':<5}")
for i, (temp, day) in enumerate(zip(lowest_values, lowest_indices), start=1):
    print(f"{i:<5} {temp:<5} {day:<5}")
