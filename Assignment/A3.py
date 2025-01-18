"""
A3
Problem Scenario:
You are provided with a dataset containing information about university students' performance over
the past three years. The dataset includes features such as attendance rate, assignment scores, 
study hours, participation in extracurricular activities, and final exam scores. 
Your objective is to analyze the data to identify key factors impacting academic performance 
and build a predictive model to forecast students' final exam scores based on these factors.
With the knowledge of scientific programming, you are required to WRITE THE SCRIPT for each task 
together with comment that explain the code.

Task 1: Data Cleaning Process
a) Examine the dataset for missing values and inconsistencies. Document how many data points
are missing for each column and explain your chosen method for handling them using Python
(pandas).
b) Detect and handle outliers in the study hours, assignment scores, and final exam scores
columns using techniques like the Interquartile Range (IQR) or Z-score method.

Task 2: Descriptive Data Analysis
a) Generate descriptive statistics (mean, median, mode, standard deviation) for the key variables:
attendance rate, assignment scores, study hours, and final exam scores. What insights can be
drawn from these statistics?
b) Perform a bivariate analysis to investigate the relationship between attendance rate, study
hours, and final exam scores. Use correlation coefficients and explain your findings.

Task 3: Data Visualization
a) Create visualizations such as histograms or box plots to represent the distribution of study
hours and final exam scores. What patterns or trends do you observe?
b) Construct a scatter plot matrix or heatmap to illustrate the relationships between attendance
rate, study hours, assignment scores, and final exam scores. Identify any notable trends or
strong correlations.

Task 4: Predictive Analysis
a) Develop a predictive model using linear regression to estimate students' final exam scores
based on attendance rate, study hours, and assignment scores. Provide a rationale for your
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
students = range(df_range)  # range(0, 100)
df_size = df.shape[1]       # 5
matrix_num = df['matrix_number']

# Task 1
null_count = df.isnull().sum()
print('Number of missing values for each column')
print(null_count)

# Finding outliers using IQR, which will be marked True in new column
for i in range(1, df_size):
    data = data_list[i]
    Q1 = df[data].quantile(0.25)
    Q3 = df[data].quantile(0.75)
    IQR = Q3 - Q1

    # Define outlier boundaries with 2.0 after tweaking
    lower_bound = Q1 -2.0 * IQR
    upper_bound = Q3 +2.0 * IQR

    # Mark outlier in seperate column
    df['attendance outlier'] = (df[data] < lower_bound) | (df[data] > upper_bound)
    df['study hours outlier'] = (df[data] < lower_bound) | (df[data] > upper_bound)
    df['assignment outlier'] = (df[data] < lower_bound) | (df[data] > upper_bound)
    df['final exam outlier'] = (df[data] < lower_bound) | (df[data] > upper_bound)

    # 1b: Handling outliers / Missing values
    # Replace outliers with NaN using loc
    df.loc[(df[data] < lower_bound) | (df[data] > upper_bound), data] = np.nan
    # df[data] = df[data].where((df[data] >= lower_bound) & (df[data] <= upper_bound), np.nan)

# Create a list to store all the values of each column
# This is to handle each data column seperately
attendance = np.array(df['attendance_rate'].values)
study = np.array(df['study_hours'].values)
assignment = np.array(df['assignment_scores'].values)
finals = np.array(df['final_exam_score'].values)

# Start interpolating by getting x-points
x_points = np.arange(df_range)

# Interpolate for attendance
valid = ~np.isnan(attendance)
missing = np.isnan(attendance)
attendance[missing] = np.interp(x_points[missing], x_points[valid], attendance[valid])
df['attendance_rate'] = attendance.round(3)     # Round off to 2 decimal values

# Interpolate for study hours
valid = ~np.isnan(study)
missing = np.isnan(study)
study[missing] = np.interp(x_points[missing], x_points[valid], study[valid])
df['study_hours'] = study.round(3)              # Round off to 2 decimal values

# Interpolate for assignment scores
valid = ~np.isnan(assignment)
missing = np.isnan(assignment)
assignment[missing] = np.interp(x_points[missing], x_points[valid], assignment[valid])
df['assignment_scores'] = assignment.round(3)    # Round off to 2 decimal values

# Interpolate for final exam
valid = ~np.isnan(finals)
missing = np.isnan(finals)
finals[missing] = np.interp(x_points[missing], x_points[valid], finals[valid])
df['final_exam_score'] = finals.round(3)        # Round off to 2 decimal values

# Export the cleaned data to new csv
df.to_csv('A3_cleaned_data.csv', index=False)

# Task 2
attendance_stats = {
    'mean' : df['attendance_rate'].mean(),
    'median' : df['attendance_rate'].median(),
    'std' : df['attendance_rate'].std()
}

study_stats = {
    'mean' : df['study_hours'].mean(),
    'median' : df['study_hours'].median(),
    'std' : df['study_hours'].std()
}

assignment_stats = {
    'mean' : df['assignment_scores'].mean(),
    'median' : df['assignment_scores'].median(),
    'std' : df['assignment_scores'].std()
}

finals_stats = {
    'mean' : df['final_exam_score'].mean(),
    'median' : df['final_exam_score'].median(),
    'std' : df['final_exam_score'].std()
}
########################
# Combine dictionaries into a single DataFrame
total_stats = {
    'attendance_rate': attendance_stats,
    'study_hours': study_stats,
    'assignment_scores': assignment_stats,
    'final_exam_score': finals_stats
}

# Create the DataFrame
stats_df = pd.DataFrame(total_stats).T
print('#################################################')
print('The statistics of each data')
print(stats_df)

# Perform a bivariate analysis on attendance rate, study hours, and final exam scores.
# Using correlation coefficients to explain findings.
def check_corr(number):
    """
    categorizes the relationship based on
    common thresholds for correlation interpretation
    """
    if number > 0.7:
        return 'Strong positive relationship'
    elif 0.3 < number <= 0.7:
        return 'Moderate positive relationship'
    elif 0.1 < number <= 0.3:
        return 'Weak positive relationship'
    elif -0.1 <= number <= 0.1:
        return 'No or negligible relationship'
    elif -0.3 <= number < -0.1:
        return 'Weak negative relationship'
    elif -0.7 <= number < -0.3:
        return 'Moderate negative relationship'
    else:
        return 'Strong negative relationship'
    
correlation1 = df['attendance_rate'].corr(df['final_exam_score'])
correlation2 = df['study_hours'].corr(df['final_exam_score'])

print('#################################################')
print(f"""
Bivariate Relationship between attendance rate and final exam score: 
    {check_corr(correlation1)}
""")

print(f"""
Bivariate Relationship between study hours and final exam score:
    {check_corr(correlation2)}
""")

# Task 3
