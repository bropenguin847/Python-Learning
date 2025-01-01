"""Used for chapter5_practice.py"""

import numpy as np


def celsius_to_fahrenheit(celsius_array):
    '''Convert Celsius array to fahrenheit '''
    return (celsius_array * 9/5) + 32

def main():
    '''Generate an array of Celsius temperatures from -20 to 100 with 10 values'''
    celsius_array = np.linspace(-20, 100, 10)
    # Convert to Fahrenheit
    fahrenheit_array = celsius_to_fahrenheit(celsius_array)
    # Print the result using f-strings
    print(f"Celsius temperatures: {celsius_array}")
    print(f"Fahrenheit temperatures: {fahrenheit_array}")

# Only execute the main function if the script is run directly
if __name__ == "__main__":
    main()

# By putting the primary code in main():, the celsius_to_fahrenheit
# function becomes reusable.
# When this script is imported into another script, only the
# celsius_to_fahrenheit function will be accessible, and the code in main()
# won’t run. This prevents unintended execution of test code or examples when
# you just want to use the conversion function.
# Checking __name__ == "__main__": main()
#     - The condition if __name__ == "__main__": main() checks whether the
#       script is being run directly or being imported.
#     - If the script is run directly, this condition is True, so main() is executed.
#     - If the script is imported, this condition is False, so main() is not executed.
