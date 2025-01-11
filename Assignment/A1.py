"""
A1
Problem Statement:
A1_dataset.csv records the monthly temperatures and precipitacion levels of three cities over
a five-year period. The goal is to use Python to clean, analyze, visualize, and build a
predictive model to forecast future temperature and precipitation levels.
Requirement: To WRITE THE SCRIPT for each task with comments that in the code with the
knowledge of scientific programming.

Task 1: Data Cleaning Process
a) Inspect the dataset for missing values and outliers. Document the number of missing
values. Outline strategy for handling them using Python libraries such as pandas.
b) Implement the cleaning steps in Python, including filling missing values using appropriate
techniques (mean, median, or interpolation) and removing or handling outliers.

Task 2: Descriptive Data Analysis
a) Generate summary statistics (mean, median, standard deviation) for the temperature and
precipitation data of each city. What do these statistics tell you about the distribution of data
for each city?
b) Analyze the relationship between temperature and precipitation using a correlation
coefficient. What can you conclude from this analysis?

Task 3: Data Visualization
a) Create visualizations that represent the distribution of temperature and precipitation over
time for each city (e.g., line plots or histograms). Include commentary on any observed trends
or patterns.
b) Construct a comparative plot (e.g., a multi-line chart) to illustrate the temperature trends
across all three cities. Highlight any seasonal variations or trends you identify.

Task 4: Predictive Analysis
a) Develop a predictive model using linear regression to forecast future temperatures and
precipitation levels based on historical data. Explain your choice of model and preprocessing
steps.
b) Evaluate the performance of your model using metrics such as R-squared or mean absolute
error (MAE). What do these metrics indicate about the model's predictive accuracy?
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('A1_dataset.csv')
data_list = list(df.columns)
df_range = df.shape[0]      # 60
df_size = df.shape[1]       # 7
month = df['month']
time = range(df_range)

color_list = ['forestgreen', 'dodgerblue', 'darkorchid',
              'firebrick', 'mediumseagreen', 'darkmagenta', 'fuchsia']

# Task 1 : Data Cleaning
# 1a: Finding missing values & outliers
null_count = df.isnull().sum()
print('Number of missing values for each city')
print(null_count)

# Using IQR method, we can find outlier based on interquartile range
# Now Outlier in each column is marked True
for i in range(1, df_size):
    data = data_list[i]
    Q1 = df[data].quantile(0.25)
    Q3 = df[data].quantile(0.75)
    IQR = Q3 - Q1

    # Define outlier boundaries with 1.5 being the standard, the value can be tweaked
    lower_bound = Q1 -1.5 * IQR
    upper_bound = Q3 +1.5 * IQR

    # Mark outlier in seperate column
    if i < 4:
        df[f'Outlier Temperature City {i}'] = (df[data] < lower_bound) | (df[data] > upper_bound)
        df[f'Outlier Precipitation City {i}'] = (df[data] < lower_bound) | (df[data] > upper_bound)
    
    # 1b: Handling outliers / Missing values
    # Replace outliers with NaN using loc
    df.loc[(df[data] < lower_bound) | (df[data] > upper_bound), data] = np.nan
    # df[data] = df[data].where((df[data] >= lower_bound) & (df[data] <= upper_bound), np.nan)

# Calculate the correlation coefficient for temperature and precipitation
    if i < 4:
        correlation = df[[f'temperature_city{i}', f'precipitation_city{i}']].corr()

        if correlation.iloc[0, 1] > 0.7:
            print(f'Strong positive correlation between temperature and precipitation in City {i}.')
        elif correlation.iloc[0, 1] < -0.7:
            print(f'Strong negative correlation between temperature and precipitation in City {i}.')
        else:
            print(f'Weak or no correlation between temperature and precipitation in City {i}.')

# Missing values can be filled using linear interpolation
# Create dictionary to store all the values of temperature and precipitation
# Since there is only three cities, the range will be from 1 to 3
temp_cities = {f'temp_city{i}': df[f'temperature_city{i}'].values for i in range(1, 4)}
preci_cities = {f'preci_city{i}': df[f'precipitation_city{i}'].values for i in range(1,4)}

# Get x points for interpolation range
x_points = np.arange(df_range)
# Interpolate all 3 cities for temperature
for city in temp_cities:
    data = temp_cities[city]
    valid = ~np.isnan(data)
    missing = np.isnan(data)

    temp_cities[city][missing] = np.interp(x_points[missing], x_points[valid], data[valid])

# Interpolate all 3 cities for precipitation
for city in preci_cities:
    data = preci_cities[city]
    valid = ~np.isnan(data)
    missing = np.isnan(data)

    preci_cities[city][missing] = np.interp(x_points[missing], x_points[valid], data[valid])

# Task 2 : Data Analysis
# 2a: Finding mean, median and standard deviation, give summary of each city
# 2b: Analyze the relationship between temperature and precipitation (with correlation coefficient)

# Use library to fill in stats for each city, such as mean, median and std deviation
city1= {
    'temperature': {
        'mean': df['temperature_city1'].mean(),
        'median': df['temperature_city1'].median(),
        'std': df['temperature_city1'].std()
    },
    'precipitation':{
        'mean': df['precipitation_city1'].mean(),
        'median': df['precipitation_city1'].median(),
        'std': df['precipitation_city1'].std()
    }
}
stats_city1 = pd.DataFrame(city1)

city2= {
    'temperature': {
        'mean': df['temperature_city2'].mean(),
        'median': df['temperature_city2'].median(),
        'std': df['temperature_city2'].std()
    },
    'precipitation':{
        'mean': df['precipitation_city2'].mean(),
        'median': df['precipitation_city2'].median(),
        'std': df['precipitation_city2'].std()
    }
}
stats_city2 = pd.DataFrame(city2)

city3= {
    'temperature': {
        'mean': df['temperature_city3'].mean(),
        'median': df['temperature_city3'].median(),
        'std': df['temperature_city3'].std()
    },
    'precipitation':{
        'mean': df['precipitation_city3'].mean(),
        'median': df['precipitation_city3'].median(),
        'std': df['precipitation_city3'].std()
    }
}
stats_city3 = pd.DataFrame(city3)

# Round all values to 3 decimal places
stats_city1 = stats_city1.round(3)
stats_city2 = stats_city2.round(3)
stats_city3 = stats_city3.round(3)

# Task 3
# 3a: Create graphs for temperature and precipitations over time for each city
for i in range(1, 4):
    plt.plot(time, temp_cities[f'temp_city{i}'], color='midnightblue', marker='x', label='Temperature')
    plt.plot(time, preci_cities[f'preci_city{i}'], color='maroon', marker='o', label='Precipitation')
    plt.title(f'Temperature & Precipitation City {i}')
    plt.legend(loc='upper left')
    plt.show()

# 3b: Create comparative plot (multi-line chart) to illustrate trends
# Plot for temperature
plt.figure(figsize=(10, 6))
for i in range(1, 4):
    plt.plot(time, temp_cities[f'temp_city{i}'], label=f'City {i}', marker='o')

plt.xlabel('Months')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Average Temperature Comparison')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot for Precipitation
plt.figure(figsize=(10, 6))
for i in range(1, 4):
    plt.plot(time, preci_cities[f'preci_city{i}'], label=f'City {i}', marker='o')

plt.xlabel('Months')
plt.ylabel('Precipitation')
plt.title('Monthly Average Precipitation Comparison')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Export the cleaned data to new csv
df.to_csv('cleaned_data.csv', index=False)

# Task 4 : Predictive Analysis
# 4a: Using linear regression to predict future temperature and precipitation levels based on data

# Predictor variable (temperature)
X = df['temperature_city1'].values
# Target variable (precipitation)
y = df['precipitation_city1'].values

# Add a column of ones to X for the bias term (intercept)
X_b = np.c_[np.ones((X.shape[0], 1)), X]

# Calculate the optimal theta (weights) using the normal equation
theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Predictions
y_pred = X_b.dot(theta)

# 4b: Evaluate model using r-squared / MAE

# Calculate Mean Absolute Error (MAE)
mae = np.mean(np.abs(y_pred - y))

# Calculate R-squared
ss_total = np.sum((y - np.mean(y))**2)
ss_residual = np.sum((y - y_pred)**2)
r2 = 1 - (ss_residual / ss_total)

# Display the evaluation metrics
print(f"Mean Absolute Error (MAE): {mae}")
print(f"R-squared: {r2}")

# Conclusion:
if r2 > 0.7:
    print("The model has a good fit with the data (R-squared > 0.7).")
else:
    print("The model's fit is not strong (R-squared < 0.7).")


# linear regression: predicting output variable based on the relationship
# between the input and output variables
