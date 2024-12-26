# Input values for a, b, and c
a = float(input('Input a value: '))
b = float(input('Input b value: '))
c = float(input('Input c value: '))

# Calculate the discriminant
d = b**2 - 4 * a * c

#########################################################
#(3) Multiple conditions if else
# Check for specific conditions
def practice3():
    if d == 0 and a != 0:
        x = -b / (2 * a)
        print(f'The value of x is: {x}')
    else:
        print('Different root')

#########################################################
#(4) Multiple conditions if elif else
# Check for conditions using if-elif-else
def practice4():
    if d == 0 and a != 0:
        x1 = -b / (2 * a)
        x2 = x1
        print(f'The roots are both: {x1}')
    elif d > 0 and a != 0:
        x1 = (-b + (d**0.5)) / (2 * a)
        x2 = (-b - (d**0.5)) / (2 * a)
        print(f'The roots are: {x1} and {x2}')
    else:
        print('Complex root')

#########################################################
#(5) Nested if statements
def practice5():
    if a != 0:
        if d == 0:
            x1 = -b / (2 * a)
            x2 = x1
            print(f'The roots are both: {x1}')
        elif d > 0:
            x1 = (-b + (d**0.5)) / (2 * a)
            x2 = (-b - (d**0.5)) / (2 * a)
            print(f'The roots are: {x1} and {x2}')
        else:
            print('Complex root')
    else:
        x1 = -c / b
        print(f'The root is: {x1}')