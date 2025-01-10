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
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from scipy.interpolate import interp1d

df = pd.read_csv('A1_dataset.csv')
city_list = list(df.columns)
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
        df[f'Outlier Precipitation City {i}'] = (df[data] < lower_bound) | (df[data] > upper_bound)

# 1b: Handling outliers / Missing values
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

# Remove outliers
############# filtered_data = data[(data >= lower_bound) & (data <= upper_bound)]

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

# Task 3
# 3a: Create graphs for temperature and precipitations over time for each city
for i in range(1, 4):
    plt.plot(time, temp_cities[f'temp_city{i}'], color='midnightblue', marker='x', label='Temperature')
    plt.plot(time, preci_cities[f'preci_city{i}'], color='maroon', marker='o', label='Precipitation')
    plt.title(f'Temperature & Precipitation City {i}')
    plt.legend(loc='upper left')
    plt.show()

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

# %%
