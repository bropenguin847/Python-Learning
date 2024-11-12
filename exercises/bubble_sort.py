""""
Bubble sort algorithm
maybe can create a excel sheet of random data, then plot the data
after that sort the data, then plot again
would be fun
"""

import numpy as np
# import pandas as pd
# import matplotlib as plt

# rows, columns = 40, 3
# data = np.random.rand(rows, columns) * 400 - 100    # Numbers between -100 and 400
# data = np.round(data, 2)
# print(data)

# df = pd.DataFrame(data, columns=[f'Column_{i+1}' for i in range(columns)])
# # Export DataFrame to Excel
# df.to_csv("random_data.csv", index=False)
# print("Data has been saved to random_data.csv")

a = [13, 14, 345, 45, 878, 48, 94, 89, 154, 48, 687, 3, 6789, 434]
n = len(a)
print(f"Before bubble sort: {a}")
i = 0
for i in range(n):
    j = 0
    while(j < n-i-1):
        place = []
        if a[j] > a[j+1]:
            place = a[j]
            a[j] = a[j+1]
            a[j+1] = place
        j += 1
    i+=1
print(f"After bubble sort: {a}")