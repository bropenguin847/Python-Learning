import random  # Import the random module to generate random numbers

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
3