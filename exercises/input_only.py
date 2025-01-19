"""
This script defines a function to safely get integer input from the user.

The `get_integer_input` function:
- Prompts the user for input using a customizable message.
- Ensures the input is an integer.
- Repeats the prompt until a valid integer is provided.

Usage:
Call `get_integer_input(prompt)` where `prompt` is the message displayed to the user.

Example:
    age = get_integer_input("Enter your age: ")
    print(f"Your age is {age}")
"""
def get_integer_input(prompt):
    """
    Prompt the user to enter an integer. Repeats until a valid integer is entered.
    Floats not accepted.
    Args:
        prompt (str): The message displayed to the user.

    Returns:
        int: The integer entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")
user_input = get_integer_input("Put a number here: ")
print(user_input)