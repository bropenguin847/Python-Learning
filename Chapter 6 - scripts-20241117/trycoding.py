# import pandas as pd
# import openpyxl
# import os
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

#############################################################################
import os
import pandas as pd

directory = os.path.dirname(__file__)
expenses_path = os.path.join(directory, "monthly_expenses.xlsx")

dataframe = pd.read_excel(expenses_path, sheet_name="Expenses")
expenses = dataframe.to_numpy()

expenses_type = []
savings_oppurtunity = []

def categorize_expense(self):
    return "High" if self > 500 else "Low"

for i in range(len(expenses)):
    expenses_type.append(categorize_expense(expenses[i,0]))
    if expenses[x,x] == "Entertainment":
        


for i in range(len(data)):
    adjusted_price.append(adjust_price(data[i,2],data[i,3])) 
    if data[i,4] >0:
        stock.append("In Stock")
    else:
        stock.append("Out of stock")
   

# Add bonus and status column to original df
df['Adjusted price']=adjusted_price
df['In/Out of stock']=stock

# Write updated df to excel file
with pd.ExcelWriter('product_catalog.xlsx', mode='a', if_sheet_exists='overlay') as writer:
    df.to_excel(writer, sheet_name='Products', index=False, header=True)