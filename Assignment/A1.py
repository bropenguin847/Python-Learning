"""
Team Connecting....

A1
Problem Statement:
A1_dataset.csv records the monthly temperatures and precipitacion levels of three cities over
a five-year period. The goal is to use Python to clean, analyze, visualize, and build a
predictive model to forecast future temperature and precipitation levels.
Requirement: To WRITE THE SCRIPT for each task with comments that in the code with the
knowledge of scientific programming.

Task 1: Data Cleaning Process
a) Inspect the dataset for missing values and outliers. Document the number of missing
values and outline your strategy for handling them using Python libraries such as pandas.
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
# from scipy.interpolate import interp1d

df = pd.read_csv('A1_dataset.csv')
city_list = list(df.columns)
df_range = df.shape[0]      # 60
df_size = df.shape[1]       # 7

month = df['month']
temp_city1 = df['temperature_city1'].values
temp_city2 = df['temperature_city2'].values
temp_city3 = df['temperature_city3'].values
preci_city1 = df['precipitation_city1'].values
preci_city2 = df['precipitation_city2'].values
preci_city3 = df['precipitation_city3'].values

color_list = ['forestgreen', 'dodgerblue', 'darkorchid',
              'firebrick', 'mediumseagreen', 'darkmagenta']
print(df.describe())


# Task 1 : Data Cleaning
# 1a: Finding missing values & outliers
null_count = df.isnull().sum()
print('Number of missing values for each city')
print(null_count)

# using IQR method, we can find outlier based on interquartile range
for i in range(1, df_size):
    data = city_list[i]
    Q1 = df[data].quantile(0.25)
    Q3 = df[data].quantile(0.75)
    IQR = Q3 - Q1

    # Define outlier boundaries with 1.5 being the standard, the value can be tweaked
    lower_bound = Q1 -1.5 * IQR
    upper_bound = Q3 +1.5 * IQR
    if i < 4:
        df[f'Outlier Temperature City {i}'] = (df[data] < lower_bound) | (df[data] > upper_bound)
    else:
        df[f'Outlier Precipitation City {i-3}'] = (df[data] < lower_bound) | (df[data] > upper_bound)
print(df)

# 1b: Handling outliers / missing values
# Missing values can be filled using linear interpolation

#%%
F = np.copy(temp_city1)
nans = np.isnan(temp_city1)
# F[nans] = np.interp(df_range[nans], df_range[~nans], temp_city1[~nans])

# Task 2 : Data Analysis
# 2a: Finding mean, median and standard deviation, give summary of each city
# 2b: Analyze the relationship between temperature and precipitation (with correlation coefficient)

# Use library to fill in stats of city, such as mean, median and std deviation
stats = {}

for i in range(1, 4):
    city = city_list[i]
    stats[i] = {
        'temperature': {
            'mean': df[f'temperature_city{i}'].mean(),
            'median': df[f'temperature_city{i}'].median(),
            'std': df[f'temperature_city{i}'].std()
        },
        'precipitation': {
            'mean': df[f'precipitation_city{i}'].mean(),
            'median': df[f'precipitation_city{i}'].median(),
            'std': df[f'precipitation_city{i}'].std()
        }
    }
stats_df = pd.DataFrame(stats)
# temp_mean = df['temperature_city1'].mean()
# temp_median = df['temperature_city1'].median()
# temp_std = df['temperature_city1'].std()
# preci_mean= df['precipitation_city1'].mean()
# preci_median = df['precipitation_city1'].median()
# preci_std= df['precipitation_city1'].std()

# Fill up with mean, median and std deviation of temperature and precipitation
# temp_city1 = [temp_mean, temp_median, temp_std]
# preci_city1 = [preci_mean, preci_median, preci_std]

# print(temp_city1)
# print(preci_city1)


# Task 3
# 3a: Create graphs for temperature and precipitations over time for each city
# 3b: Create comparative plot (multi-line chart) to illustrate trends

# Create subplots (top: original data with NaN values, bottom: data after filling NaN values)
# fig, (temperature_plot, precipitation_plot) = plt.subplots(2, 1, figsize=(8, 8))


# for i in range(1, df_size):
#     data = city_list[i]
#     df.plot(x='month', y=data, color=color_list[i-1])       # add kind= to change kind of plot
#     plt.legend(loc='lower left')
# plt.show()





# Task 4 : Predictive Analysis
# 4a: Using linear regression to predict future temperature and precipitation levels based on data
# 4b: Evaluate model using r-squared / MAE

# linear regression: predicting output variable based on the relationship
# between the input and output variables
