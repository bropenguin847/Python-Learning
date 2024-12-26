import pandas as pd

def categorize_expense (amount):
    if amount >500:
        return "High"
    else:
        return "Low"

df = pd.read_excel('monthly_expenses.xlsx', sheet_name='Expenses')

data = df.to_numpy()

expenses_type=[]
saving_opportunity=[]

for i in range(len(data)):
    expenses_type.append(categorize_expense(data[i,2])) 
    if data[i,1]== "Entertainment" and data[i,2] >500 :
        saving_opportunity.append("Yes")
    else:
        saving_opportunity.append("No")
   
df['Expenses type']=expenses_type
df['Saving opportunity']=saving_opportunity

with pd.ExcelWriter('monthly_expenses.xlsx', mode='a', if_sheet_exists='overlay') as writer:
    df.to_excel(writer, sheet_name='Expenses', index=False, header=True)