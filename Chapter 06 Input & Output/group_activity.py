# Scenario 1: Calculating Annual Bonus
import numpy as np
import pandas as pd
import openpyxl
import os
current_dir = os.path.dirname(__file__)     # Declaring directory to read file

employee_path = os.path.join(current_dir, 'employee_data.xlsx')
score_path = os.path.join(current_dir, 'student_scores.xlsx')
year = pd.read_excel(employee_path, sheet_name='Details', header=0).iloc[0:, 3]
length = len(year)
# data = pd.read_excel(employee_path, sheet_name='Details', header=0)
# year["Years with Company"] <- ask David the Goliath Slayer
bonus_list = []
def calculate_bonus():
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