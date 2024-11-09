# Values for the principal amounts
a_values = [100, 500, 800]
# Values for the number of years
n_values = [2, 4, 6, 8, 10]
# Interest rate
r = 0.09

# Loop through each value of a
for a in a_values:
    # Loop through each value of n
    for n in n_values:
        # Calculate the final balance using the compound interest formula
        B = a * (1 + r) ** n
        # Print the results
        print(f"For a = {a}, n = {n}, B = {B:.2f}")
