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


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Set the current directory to the current file path
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'A3_dataset.csv')
df = pd.read_csv('A3_dataset.csv')

data_list = list(df.columns)
df_range = df.shape[0]      # 100
students = range(df_range)  # range(0, 100)
df_size = df.shape[1]       # 5
matrix_num = df['matrix_number']

# Task 1
null_count = df.isnull().sum()
# df.isna().index.tolist()
np.nancumsum
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

"""
1. Attendance Rate Mean: 80.84; Median: 82.20; Standard Deviation: 10.63
The value of mean and median is very close means that the distribution of attendance rates is relatively symmetric and not skewed. 
A standard deviation value of 10.63 indicates that there is considerable variation in attendance rates across the sample. This shows that the attendance rates of some students deviate around 11.82  from the mean of attendance rates. 
2. Study Hours Mean: 9.94, Median: 10.10, Standard Deviation: 1.78
The mean and median are very close apart to each other suggesting a consistent trend  and very low skewed in the data.
The low standard deviation of 1.78 indicates that the study hours of most students for a week is most likely the same.
3. Assignment Scores Mean: 76.14; Median: 77.05, Standard Deviation: 14.37
The mean and median are almost the same, indicating the symmetricity of the data and small skewness.
However, higher standard deviation of 14.37 has suggested that some of the students might struggle to excel in assignment.Hence, performance inconsistency may occur in many of the students causing them not performing well in their assignment.
4.Final Exam Mean: 53.30, Median: 54.40, Standard Deviation: 7.70. 
The mean and median are rather close to each other, which indicates that final exam scores are symmetrically distributed.
A standard deviation of 7.70 would signify moderate variability in exam scores such that students might have performed differently due to study habits, attendance, or understanding of the material.
"""

# Perform a bivariate analysis on attendance rate, study hours, and final exam scores.
# Using correlation coefficients to explain findings.
def check_corr(number):
    """
    Categorizes the relationship based on
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

"""
Result:
 Bivariate Relationship between attendance rate and final exam score: 
      Moderate positive relationship
    

      Bivariate Relationship between study hours and final exam score:
      Strong positive relationship

Finding:
Attendance and Exam Performance:
Improving attendance consistency might lead to better performance in exams as the students will not miss out on what the lecturer has taught during the lecture if the student has frequently attended the lecture.

Study Hours and Exam Scores:
This suggests that study hours is very important in scoring a high score in the final exam. Thus, we should focus on study quality and study method instead.
"""

# Task 3:Data Visualization
# 3a:Visualizations to represent the distribution 
# Create a box plot to visualize the data of study hours and final exam scores
plt.figure(figsize=(10, 5))

# Boxplot for study hours
plt.subplot(1, 2, 1)
plt.boxplot(df['study_hours'].dropna()) # to ensure cleaned data
plt.title('Box Plot of Study Hours')
plt.xlabel('Study Hours')

# Boxplot for Final exam scores
plt.subplot(1, 2, 2)
plt.boxplot(df['final_exam_score'].dropna()) # to ensure cleaned data
plt.title('Box Plot of Final Exam Scores')
plt.xlabel('Final Exam Scores')

plt.tight_layout()
plt.show()

'''
Insights:
Both variables have their median located close to the center of the box, indicating a relatively symmetrical distribution for both study hours and final exam scores.
Study hours may contribute to differences in final exam scores, which can be explored further with correlation coefficients presented in heatmap.
    
'''
# 3b:Use heatmap to illustrate the relationships between variables
# Create a correlation matrix
columns_data = ['attendance_rate', 'study_hours', 'assignment_scores', 'final_exam_score']
correlation_matrix = np.matrix(df[columns_data].corr().values)

# Create heatmap for the correlation coefficient
plt.figure(figsize=(8, 6))
plt.imshow(correlation_matrix,cmap='autumn')

labels = ['Attendance rate','Study hours','Assignment scores','Final exam score']
plt.xticks(range(len(labels)), labels)
plt.yticks(range(len(labels)), labels)

# Annotate the correlation value into each cell
for i in range(len(labels)):
    for j in range(len(labels)):
        plt.text(j, i, f"{correlation_matrix[i, j]:.2f}")

plt.title("Heatmap of Correlation relationship")
plt.tight_layout()
plt.show()

'''
From the correlation coefficient shown in the heatmap,we could find that there is a strong correlation between Study Hours and Final Exam Score (correlation value: 0.83). This suggests that students who spend more time studying tend to perform better in the final exam.
'''
# Task 4: Predictive Analysis
# 4a:Develop a predictive model
'''
np.linalg.lstsq is designed to directly solve this problem by finding the coefficients.
This can minimize the sum of squared errors using the least squares method and provides a closed-form solution to the problem, which is both efficient and easy to implement.
Besides,np.linalg.lstsq can handle non-square matrices (when the number of features is greater than the number of samples or vice versa). 
This has made it very flexible in handling a variety of regression problems, including regularized regression or ridge regression.
'''
# Select the relevant features and target variable (final_exam_score)
X = df[['attendance_rate', 'study_hours', 'assignment_scores']].values
y = df['final_exam_score'].values

#Add a column of ones to the features as an intercept term(bias)
X = np.c_[np.ones(X.shape[0]), X] 

#Perform Linear Regression using numpy.linalg.lstsq to solves the equation
coefficients, residuals, rank, s = np.linalg.lstsq(X, y)

#Regression coefficients which includes the intercept
print('#################################################')
print("Regression Coefficients (including intercept):")
print(coefficients) 
'''
Intercept: 13.57085848 
Attendance Rate Coefficient: 0.03812713
Study Hours Coefficient: 3.46613507
Assignment Scores Coefficient: 0.02868089
'''

#Predict the final exam scores using the model
y_predict = X.dot(coefficients)


# 4b:Evaluation of the model 
# Calculate R-squared
total_sos = np.sum((y - np.mean(y)) ** 2)  # Total sum of squares
residual_sos = np.sum((y - y_predict) ** 2)  # Residual sum of squares
r_squared = 1 - (residual_sos / total_sos)

# Calculate Mean Absolute Error (MAE)
mae = np.mean(np.abs(y - y_predict))

print(f"R-squared: {r_squared:.3f}") #0.695
print(f"Mean Absolute Error (MAE): {mae:.4f}") #3.3498
print('#################################################')
'''
R-squared:0.695
Mean Absolute Error (MAE):3.3498

These regression coefficients has shows the correlation of features to the final exam score:
Study Hours has the largest coefficient (3.47) which mean that it has the strongest correlations with final exam scores
Attendance Rate (0.038)  and Assignment Scores (0.029) have relatively small coefficients meaning that it has weaker correlations with final exam scores.

R-squared (Coefficient of determination)
The R-squared of 0.695 means that the 69.5% of variability is explained by the model

Mean Absolute Error (MAE):
The MAE of 3.3498 means the predicted final exam scores deviate from the actual scores by 3.3498. 
'''


# Task 4 extra
# Find the estimate of final exam score and attendance rate
# Predict final exam score based on:
# Attendance = 85.7
# Study hours = 12.3
# Assignment score = 77.7
elements = [attendance, study, assignment]
prediction = [85.7, 12.3, 77.7]
future = []

def linfunc(x):
  """
  Takes an input value x and applies the linear regression equation
  (slope * x + intercept) to predict the corresponding value
  based on the data. It uses the slope and intercept obtained
  from the linregress function.
  """
  return slope * x + intercept

for i, element in enumerate(elements):
    slope, intercept, r, p, std_err = stats.linregress(element, finals)
    model = list(map(linfunc, element))
    future.append(linfunc(prediction[i]))

    print(f'Relationship : {r}')
    plt.scatter(element, finals)
    plt.plot(element, model)
    plt.show()

print('Prediction of future value')
print(f'If attendance is 85.7, Final exam score will be {future[0]}')
print(f'If study hours is 12.3, Final exam score will be {future[1]}')
print(f'If assignment score is 77.7, Final exam score will be {future[2]}')


##################
columns_data = ['attendance_rate', 'study_hours', 'assignment_scores', 'final_exam_score']
correlation_matrix = np.matrix(df[columns_data].corr().values)

# Create heatmap for the correlation relationship
plt.figure(figsize=(8, 6))
plt.imshow(correlation_matrix,cmap='plasma')

labels = ['Attendance rate','Study hours','Assignment scores','Final exam score']
plt.xticks(range(len(labels)), labels)
plt.yticks(range(len(labels)), labels)

# Annonate the correlation value into each cell
for i in range(len(labels)):
    for j in range(len(labels)):
        plt.text(j, i, f"{correlation_matrix[i, j]:.2f}")

plt.title("Heatmap of Correlation relationship")
plt.tight_layout()
plt.show()
