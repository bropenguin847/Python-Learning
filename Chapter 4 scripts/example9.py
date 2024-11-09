# Define the initial investment and interest rate
a = 100  # Initial investment amount in dollars
r = 0.08  # Annual interest rate

# Initialize the starting year and the step
n = 2

# Use a while loop to calculate for each specified year (2, 4, 6, 8, 10)
while n <= 10:
    B = a * (1 + r) ** n  # Calculate the final balance using the compound interest formula
    print(f'n = {n}, B = {B:.2f}')  # Display the year and the calculated balance
    n += 2  # Increment the year by 2
