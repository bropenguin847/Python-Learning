'''
Team Connecting....

Problem Scenario:
You are given a dataset containing monthly sales data of an e-commerce company over the past five
years, along with data on advertising expenditure, customer reviews, and website traffic. Your task is
to analyze the data to understand sales trends, identify key factors affecting sales, and build a
predictive model to forecast future sales based on these influencing factors. With the knowledge of
scientific programming, you are required to WRITE THE SCRIPT for each task together with comment
that explain the code.
Requirement: To WRITE THE SCRIPT for each task with comments that in the code.

Task 1: Data Cleaning Process
a) Inspect the dataset for any missing or inconsistent data. Report the number of missing values
and describe your approach to handling them using Python (pandas and numpy).
b) Identify and handle any outliers in the sales, advertising expenditure, and website traffic data
using appropriate Python methods (e.g., Z-score, IQR).

Task 2: Descriptive Data Analysis
a) Generate and interpret summary statistics (mean, median, mode, standard deviation) for the
sales, advertising expenditure, and website traffic. What do these statistics reveal about the
data distribution?
b) Perform a bivariate analysis to investigate the relationships between advertising expenditure,
website traffic, and sales. Use correlation coefficients to support your findings.

Task 3: Data Visualization
a) Create visualizations such as line plots and bar charts to display the trends in monthly sales
over time and compare them to advertising expenditure and website traffic. Comment on any
paƩerns you observe.
b) Construct a multi-variable scaƩer plot or heatmap to illustrate the relationships between sales,
advertising expenditure, and website traffic. Highlight any notable correlations or trends.

Task 4: Predictive Analysis
a) Build a predictive model using multiple linear regression to forecast future sales based on
advertising expenditure and website traffic. Justify your choice of model and outline any data
preprocessing steps you took.
b) Assess the performance of your model using R-squared and Mean Squared Error (MSE).
Discuss what these metrics indicate about the accuracy and reliability of the model’s
predictions.
'''

import pandas as pd
import matplotlib.pyplot as plt

# Task 1
# Data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
cars_sold = [3, 4, 5, 3, 7, 6, 4]  # Number of cars sold each day

# Generate stacked "x" markers for each day
for i, count in enumerate(cars_sold):
    plt.scatter([i] * count, range(1, count + 1), marker='x', color='black')

# Customize the plot
plt.xticks(range(len(days)), days)  # Set x-axis labels
plt.yticks([])  # Remove y-axis labels
plt.title("Number of Cars Sold")
plt.xlabel("Days")
plt.ylabel("Number of Cars")

# Show the plot
plt.show()
# Task 2






# stats = {}
# for i in range(1, 4):
#     city = city_list[i]
#     stats[i] = {
#         'temperature': {
#             'mean': df[f'temperature_city{i}'].mean(),
#             'median': df[f'temperature_city{i}'].median(),
#             'std': df[f'temperature_city{i}'].std()
#         },
#         'precipitation': {
#             'mean': df[f'precipitation_city{i}'].mean(),
#             'median': df[f'precipitation_city{i}'].median(),
#             'std': df[f'precipitation_city{i}'].std()
#         }
#     }
# stats_df = pd.DataFrame(stats)
