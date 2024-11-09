# Loop through numbers from 1 to 50
for n in range(1, 51):
    # Check if n is not divisible by 7
    if n % 7 != 0:
        continue  # Skip the rest of the loop if n is not divisible by 7
    
    # Print the number if it is divisible by 7
    print(f"Divisible by 7: {n}")
