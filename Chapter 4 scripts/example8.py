# Define the initial investment and interest rate
a = 100  # Initial investment amount in dollars
r = 0.08  # Annual interest rate

# Loop over the specified years (2, 4, 6, 8, 10)
for n in range(2, 11, 2):
    B = a * (1 + r) ** n  # Calculate the final balance using the compound interest formula
    print(f'n = {n}, B = {B:.2f}')  # Display the year and the calculated balance
