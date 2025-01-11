"""
Scenario 1: Calculating Annual Bonus
"""

import os
import numpy as np
import pandas as pd
import openpyxl

current_dir = os.path.dirname(__file__)     # Declaring directory to read file

employee_path = os.path.join(current_dir, 'employee_data.xlsx')
score_path = os.path.join(current_dir, 'student_scores.xlsx')
year = pd.read_excel(employee_path, sheet_name='Details', header=0).iloc[0:, 3]
length = len(year)
bonus_list = []

def calculate_bonus():
    """Returns bonus calculated based on years in company"""
    if year > 5:
        return salary * 0.1
    else:
        return 0.05 * salary

index = 0
while index < length:
    year = pd.read_excel(employee_path, sheet_name='Details', header=0).iloc[index, 3]
    salary = pd.read_excel(employee_path, sheet_name='Details', header=0).iloc[index, 2]
    bonus = calculate_bonus()
    bonus_list.append(bonus)
    index += 1

bonus_list.insert(0, "Bonus")
with pd.ExcelWriter(employee_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
    output_data = pd.DataFrame([bonus_list]).T
    output_data.to_excel(writer, sheet_name='Details', startcol=4, startrow=0, index=False, header=False)

# current_dir = os.path.dirname(__file__)
# employee_path = os.path.join(current_dir, 'employee_data.xlsx')
# year = pd.read_excel(employee_path, sheet_name='Details', header=0).iloc[0:, 3]
# department=pd.read_excel(employee_path, sheet_name='Details', header=0).iloc[0:, 1]
# length = len(year)
# bonus_list = []
# status_list=[]
# def calculate_bonus():
#     if year > 5:
#         return salary * 0.1
#     else:
#         return 0.05 * salary

# def department_status():
#     if department.strip().lower() == "sales":
#         return "Target"
#     else:
#         return "Non-Target"
# # index = 0
# # while index < length:
# for index in range(len(year)):
#     year = pd.read_excel(employee_path, sheet_name='Details', header=0).iloc[index, 3]    
#     salary = pd.read_excel(employee_path, sheet_name='Details', header=0).iloc[index, 2]
#     department=pd.read_excel(employee_path, sheet_name='Details', header=0).iloc[index , 1]

#     bonus = calculate_bonus()
#     status = department_status()
#     bonus_list.append(bonus)
#     status_list.append(status)
#     index += 1

# bonus_list.insert(0, "Bonus")
# status_list.insert(0,"Status")
# with pd.ExcelWriter(employee_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
#     output_data = pd.DataFrame([bonus_list]).T
#     output_data.to_excel(writer, sheet_name='Details', startcol=5, startrow=0, index=False, header=False)
#     output_data_2= pd.DataFrame([status_list]).T
#     output_data_2.to_excel(writer, sheet_name='Details', startcol=5, startrow=0, index=False, header=False)

