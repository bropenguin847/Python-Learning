"""
Chapter 4 Example 12 & 13
continue & break statement
"""

import random  # Import the random module to generate random numbers

# Loop through numbers from 1 to 50
for n in range(1, 51):
    # Check if n is not divisible by 7
    if n % 7 != 0:
        continue  # Skip the rest of the loop if n is not divisible by 7
    
    # Print the number if it is divisible by 7
    print(f"Divisible by 7: {n}")

# Using break statement
# Generate a random number between 1 and 6
x = random.randint(1, 6)
n = 0  # Initialize the number of attempts

# Infinite loop to prompt the user for guesses
while True:
    guess = int(input('Guess the number: '))  # Ask the user to guess the number
    n += 1  # Increment the attempt count

    # Check if the guessed number is correct
    if guess == x:
        print(f'You got it right after {n} try{"s" if n > 1 else ""}!')
        break  # Exit the loop when the correct guess is made
