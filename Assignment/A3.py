"""
A3
Problem Scenario:
You are provided with a dataset containing information about university students' performance over
the past three years. The dataset includes features such as aƩendance rate, assignment scores, study
hours, participation in extracurricular activities, and final exam scores. Your objective is to analyze the
data to identify key factors impacting academic performance and build a predictive model to forecast
students' final exam scores based on these factors. With the knowledge of scientific programming, you
are required to WRITE THE SCRIPT for each task together with comment that explain the code.

Task 1: Data Cleaning Process
a) Examine the dataset for missing values and inconsistencies. Document how many data points
are missing for each column and explain your chosen method for handling them using Python
(pandas).
b) Detect and handle outliers in the study hours, assignment scores, and final exam scores
columns using techniques like the Interquartile Range (IQR) or Z-score method.

Task 2: Descriptive Data Analysis
a) Generate descriptive statistics (mean, median, mode, standard deviation) for the key variables:
aƩendance rate, assignment scores, study hours, and final exam scores. What insights can be
drawn from these statistics?
b) Perform a bivariate analysis to investigate the relationship between aƩendance rate, study
hours, and final exam scores. Use correlation coefficients and explain your findings.

Task 3: Data Visualization
a) Create visualizations such as histograms or box plots to represent the distribution of study
hours and final exam scores. What paƩerns or trends do you observe?
b) Construct a scaƩer plot matrix or heatmap to illustrate the relationships between aƩendance
rate, study hours, assignment scores, and final exam scores. Identify any notable trends or
strong correlations.

Task 4: Predictive Analysis
a) Develop a predictive model using linear regression to estimate students' final exam scores
based on aƩendance rate, study hours, and assignment scores. Provide a rationale for your
choice of model and describe the data preprocessing steps taken.
b) Evaluate the predictive model using metrics such as R-squared and Mean Absolute Error
(MAE). Discuss what these results imply about the accuracy and reliability of the model.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('A3_dataset.csv')
data_list = list(df.columns)
df_range = df.shape[0]      # 100 
df_size = df.shape[1]       # 5
matrix_num = df['matrix_number']

number = range(df_range)

# Task 1
null_count = df.isnull().sum()
print('Number of missing values for each column')
print(null_count)

for i in range(1, df_size):
    data = data_list[i]
    Q1 = df[data].quantile(0.25)
    Q3 = df[data].quantile(0.75)
    IQR = Q3 - Q1

    # Define outlier boundaries with 1.5 being the standard, the value can be tweaked
    lower_bound = Q1 -1.5 * IQR
    upper_bound = Q3 +1.5 * IQR

    # Mark outlier in seperate column
    df['attendance outlier'] = (df[data] < lower_bound) | (df[data] > upper_bound)
    df['study hours outlier'] = (df[data] < lower_bound) | (df[data] > upper_bound)
    df['assignment outlier'] = (df[data] < lower_bound) | (df[data] > upper_bound)
    df['final exam outlier'] = (df[data] < lower_bound) | (df[data] > upper_bound)

    # 1b: Handling outliers / Missing values
    # Replace outliers with NaN using loc
    df.loc[(df[data] < lower_bound) | (df[data] > upper_bound), data] = np.nan
    # df[data] = df[data].where((df[data] >= lower_bound) & (df[data] <= upper_bound), np.nan)
