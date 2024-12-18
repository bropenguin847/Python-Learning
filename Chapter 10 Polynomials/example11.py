import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the provided Excel file, skipping the first row of labels
file_path = 'internetusage.xlsx'  # Ensure the file is in the same directory or adjust the path accordingly
df = pd.read_excel(file_path, skiprows=1)

# Extracting the usage data (rows are persons, columns are months)
data = df.iloc[:, 1:7].values  # Extract data from columns B to G (1st to 6th month)

# Define months as a vector (1 to 6)
months = np.arange(1, 7)

# Replicate the month vector to match the shape of the data matrix (5 rows for 5 persons)
month_matrix = np.tile(months, (data.shape[0], 1))

# Apply polynomial fitting for each degree (1st, 2nd, 3rd)
p1 = np.polyfit(month_matrix.flatten(), data.flatten(), 1)
p2 = np.polyfit(month_matrix.flatten(), data.flatten(), 2)
p3 = np.polyfit(month_matrix.flatten(), data.flatten(), 3)

# Evaluate the average using the polynomial coefficients for months 1 to 6
average1 = np.polyval(p1, months)
average2 = np.polyval(p2, months)
average3 = np.polyval(p3, months)

# Predicting internet usage for months 7, 8, and 9
months_predict = np.array([7, 8, 9])
usage_predict_1st_order = np.polyval(p1, months_predict)
usage_predict_2nd_order = np.polyval(p2, months_predict)
usage_predict_3rd_order = np.polyval(p3, months_predict)

# Display the predictions for months 7, 8, and 9
print(f"Predicted internet usage (hours) for months 7, 8, 9 (1st Order Polynomial): {usage_predict_1st_order}")
print(f"Predicted internet usage (hours) for months 7, 8, 9 (2nd Order Polynomial): {usage_predict_2nd_order}")
print(f"Predicted internet usage (hours) for months 7, 8, 9 (3rd Order Polynomial): {usage_predict_3rd_order}")

# Plot the original data and the polynomial fits
plt.plot(months, data.T, 'o', label='Original Data')  # Transpose data to match months
plt.plot(months, average1, '--k', label='1st Degree Fit')  # Solid line for fitting months 1-6
plt.plot(months, average2, '-.b', label='2nd Degree Fit')
plt.plot(months, average3, '-r', label='3rd Degree Fit')

# Plot the predictions for months 7, 8, and 9
plt.plot(np.concatenate([months, months_predict]), 
         np.concatenate([average1, usage_predict_1st_order]), 
         'k--', label='1st Degree Prediction', alpha=0.6)  # Semi-transparent for prediction

plt.plot(np.concatenate([months, months_predict]), 
         np.concatenate([average2, usage_predict_2nd_order]), 
         'b-.', label='2nd Degree Prediction', alpha=0.6)  # Dot-dash6 line for prediction

plt.plot(np.concatenate([months, months_predict]), 
         np.concatenate([average3, usage_predict_3rd_order]), 
         'r--', label='3rd Degree Prediction', alpha=0.6)  # Dashed line for prediction

# Adjust title, labels, and grid
plt.title('Internet Usage and Polynomial Fits with Predictions')
plt.xlabel('Month')
plt.ylabel('Usage (hours)')

# Make the legend smaller with the fontsize argument
plt.legend(loc='upper left', fontsize='6')  # Use 'small', 'x-small', or a specific size like 8
plt.grid(True)
plt.show()