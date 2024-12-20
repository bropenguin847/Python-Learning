import pandas as pd
import os

current_dir = os.path.dirname(__file__)

# Scenario 4: Monthly Expense Tracker
expenses_path = os.path.join(current_dir, "monthly_expenses.xlsx")

dataframe = pd.read_excel(expenses_path, sheet_name = "Expenses")
expenses = dataframe.to_numpy()

expenses_type = []
savings_oppurtunity = []

def categorize_expense(amount):
    return "High" if amount > 500 else "Low"

for i in range(len(expenses)):
    expenses_type.append(categorize_expense(expenses[i,2]))
    if expenses[i, 1] == "Entertainment":
        savings_oppurtunity.append("Yes")
    else:
        savings_oppurtunity.append("No")

# Add bonus and status column to original dataframe
dataframe["Expenses Type"] = expenses_type
dataframe["Savings Oppurtunity"] = savings_oppurtunity

# Write updated df to excel file
with pd.ExcelWriter(expenses_path, mode='a', if_sheet_exists='overlay') as writer:
    dataframe.to_excel(writer, sheet_name = "Expenses", index=False, header=True)

##########################################################################################
# Scenario 5: Customer Feedback Analysis
customer_path = os.path.join(current_dir, "customer_feedback.xlsx")
feedback = pd.read_excel(customer_path, sheet_name = "Feedback")

# Defining functions
def categorize_feedback(rating):
    if rating >= 4:
        return "Positive"
    elif rating == 3:
        return "Neutral"
    else:
        return "Negative"

def follow_up(self):
    return "Yes" if self == "Negative" else "No"

# Creates a new column called category, then execute function categorize_feedback
feedback["Category"] = feedback["Rating"].apply(categorize_feedback)

# Creates a new column called Follow Up
feedback["Follow Up Required"] = feedback["Category"].apply(follow_up)

# Writes output to excel file
feedback.to_excel(customer_path, sheet_name = "Feedback", index = False)

##########################################################################################
# Scenario 6: Sales Performance Tracker
sales_path = r"C:\Users\brope\OneDrive\Desktop\UTM scientific programming\Chapter 6 - scripts-20241117\sales_data.xlsx"
sales = pd.read_excel(sales_path, sheet_name = "Sales")

def evaluate_performance(amount):
    if amount >= 10000:
        return "Excellent"
    elif 5000 < amount < 9999:
        return "Good"
    else:
        return "Needs Improvement"

# Create a new column called Performance
# Apply evaluate_performance function into the Sales Amount column
sales['Performance'] = sales['Sales Amount'].apply(evaluate_performance)

# Create a new column called Bonus Eligible
# Apply lambda function into the Performance column
# Lambda represent any function and x represent the value inside the column
# If x = excellent print Yes and virse versa
sales['Bonus Eligible'] = sales['Performance'].apply(lambda x: "Yes" if x == "Excellent" else "No")

sales.to_excel(sales_path, sheet_name = "Sales")