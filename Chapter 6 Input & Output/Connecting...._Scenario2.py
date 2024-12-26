import numpy as np
import pandas as pd
import os
current_dir = os.path.dirname(__file__)
scores_path = os.path.join(current_dir, 'student_scores.xlsx')
scores = pd.read_excel(scores_path, sheet_name='Scores', header=0).iloc[0:, 2]
scores_list=[]
pass_or_fail_list=[]
def assign_grade(scores):
    if scores >= 90:
        return'A'
    elif 80<=scores<=89:
        return 'B'
    elif 70<=scores<=79:
        return 'C'
    elif 60<=scores<=69:
        return 'D'
    else:
        return 'F'

def assign_pass_or_fail(scores):
    if scores>=70:
        return "Pass"
    else:
        return"Fail"

for i in range(len(scores)):
    scores_list.append(assign_grade(scores[i]))
    pass_or_fail_list.append(assign_pass_or_fail(scores[i]))
    
scores_list.insert(0, "Scores")
pass_or_fail_list.insert(0,"Pass/Fail")
with pd.ExcelWriter(scores_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
    output_data = pd.DataFrame([scores_list]).T
    output_data.to_excel(writer, sheet_name='Scores', startcol=3, startrow=0, index=False, header=False)
    output_data_2= pd.DataFrame([pass_or_fail_list]).T
    output_data_2.to_excel(writer, sheet_name='Scores', startcol=4, startrow=0, index=False, header=False)
