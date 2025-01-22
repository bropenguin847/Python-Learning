"""
Chapter 4 Example 8 & 9
for loop and while loop
"""

# Define the initial investment and interest rate
A = 100  # Initial investment amount in dollars
R = 0.08  # Annual interest rate

# Using for loop over the specified years (2, 4, 6, 8, 10)
for n in range(2, 11, 2):
    B = A * (1 + R) ** n  # Calculate the final balance using the compound interest formula
    print(f'n = {n}, B = {B:.2f}')  # Display the year and the calculated balance

########################################################################
# Using While loop
# Initialize the starting year and the step
NUM = 2

# Use while loop to calculate for each specified year (2, 4, 6, 8, 10)
while NUM <= 10:
    B = A * (1 + R) ** n  # Calculate the final balance using the compound interest formula
    print(f'n = {n}, B = {B:.2f}')  # Display the year and the calculated balance
    NUM += 2  # Increment the year by 2
