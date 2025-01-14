"""
Set 3
A city measures the average monthly air quality index (AQI) over the past year.
The data is stored in a xlsx file named air_quality.xlsx:

1.	Write a Python script to load the data from air_quality.xlsx and perform
    polynomial curve fitting for the AQI using polynomial orders 1, 2, 3 and 4.
2.	Using the fitted models, predict the AQI for the next three month_array
    (January, February, and March of the following year).
3.	Create a user interface for the users to select which order they want to display in the graph.
    Example; 1 = order 1, 2 = order 2, 3 = order 3 or 4 = order 1,2 and 3.
4.	Plot the original data and overlay the polynomial fitting curves on the same graph
    based on user selection.

Using the best-fit polynomial model from above, calculate and display the AQI for the
first three month_array of the next year in a Python console table.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Task 1 Load data and fitting
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'air_quality.xlsx')
df = pd.read_excel(file_path)       # Creating dataframe

aqi = df['AQI'].values
size = df.shape[0]                          # 12
month_array = np.arange(0, size)            # [0,1,2,3,4,5,6,7,8,9,10,11]
months_extend = np.arange(0, size + 3)      # [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

month_name = list(df['Month'])
extra_name = ['January x', 'February x', 'March x']
month_name.extend(extra_name)
#['January', 'February', 'March', 'April', 'May','June','July','August','September',
# 'October','November','December','Jan x','Feb x','Mar x']

# Get polyfit for order 1 - 4
fit1 = np.polyfit(month_array, aqi, 1)
fit2 = np.polyfit(month_array, aqi, 2)
fit3 = np.polyfit(month_array, aqi, 3)
# fit4 = np.polyfit(month_array, aqi, 4)

# Get polyval for month_array 0 to 11
average1 = np.polyval(fit1, month_array)
average2 = np.polyval(fit2, month_array)
average3 = np.polyval(fit3, month_array)
# average4 = np.polyval(fit4, month_array)

# Task 2 Predicting for next three month_array
# Since index of December is 11, next three month_array is 11 + 3 = 4
months_predict = np.array([12, 13, 14])
predit_order1 = np.polyval(fit1, months_predict)
predit_order2 = np.polyval(fit2, months_predict)
predit_order3 = np.polyval(fit3, months_predict)
# predit_order4 = np.polyval(fit4, months_predict)

extended1 = np.concatenate([average1, predit_order1])
extended2 = np.concatenate([average2, predit_order2])
extended3 = np.concatenate([average3, predit_order3])
# extended4 = np.concatenate([average4, predit_order4])

plt.plot(months_extend, extended1, color='darkorange', label='Fitted order 1', marker='x')
plt.plot(months_extend, extended2, color='mediumseagreen', label='Fitted order 2', marker='x')
plt.plot(months_extend, extended3, color='darkmagenta', label='Fitted order 3', marker='x')
# plt.plot(months_extend, extended4, color='dodgerblue', label='Fitted order 4')
plt.legend()
plt.title('Polyfit all order')
plt.xlabel('Months')
plt.xticks(months_extend, labels=month_name, rotation=50)
plt.ylabel('AQI')
plt.show()

# Task 3 Get user input
def get_input():
    """Gets integer input from user, and will prompt user if wrong input"""
    while True:
        try:
            num = int(input("""
                            What polynomial order you want?: Enter your number.
                            - Enter (1) for order 1
                            - Enter (2) for order 2
                            - Enter (3) for order 3
                            - Enter (4) for order 1, 2 & 3
                            """))
            if 1 <= num <= 4:
                return num
            else:
                print("Please enter a number between 1 and 4")
        except ValueError:
            print('Please enter a valid order from 1 - 4')
order = get_input()

# Task 4 Plot original data and overlay
if order == 1:
    print('Plot for polyfit order 1')
    plt.plot(months_extend, extended1, color='navy', label=f'Fitted order {order}', marker='x')
elif order == 2:
    print('Plot for polyfit order 2')
    plt.plot(months_extend, extended2, color='royalblue', label=f'Fitted order {order}', marker='x')
elif order == 3:
    print('Plot for polyfit order 3')
    plt.plot(months_extend, extended3, color='mediumslateblue', label=f'Fitted order {order}', marker='x')
else:
    print('Plot for all order of polyfit')
    plt.plot(months_extend, extended1, color='darkgreen', label=f'Fitted order {order}', marker='x')
    plt.plot(months_extend, extended2, color='royalblue', label=f'Fitted order {order}', marker='x')
    plt.plot(months_extend, extended3, color='goldenrod', label=f'Fitted order {order}', marker='x')

plt.plot(month_array, aqi, color='tomato', label='Original', marker='o')
plt.xlim(0, 15)
plt.title('Set 3')
plt.xticks(months_extend, labels=month_name, rotation=50)
plt.xlabel('Months')
plt.ylabel('AQI')
plt.tight_layout()
plt.legend(loc='lower left')
plt.show()
