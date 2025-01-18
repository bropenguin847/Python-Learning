import random

def is_odd(number):
    """
    Worst is odd statement ever
    """
    incrementor = 1
    is_incrementor_odd = True
    while incrementor < number:
        incrementor += 1
        if is_incrementor_odd:
            is_incrementor_odd = False
        else:
            is_incrementor_odd = True

    return is_incrementor_odd

num = int(input('Give a random number'))
print(f'Is {num} an odd number: {is_odd(num)}')
