"""
Chapter 3 Example 11
Operator Precedence

Operator precedence determines the order in which operations are performed in an expression.
It's a set of rules that dictate which operation goes first when there are
multiple operators in a single expression.
Think of it as the order of operations in mathematics (PEMDAS/BODMAS).

For instance, in the expression 2 + 3 * 4, multiply (*) has higher precedence than addition (+).
Therefore, the multiplication is performed before the addition:
"""

# Sample variables
a = 5
b = 2
c = 3

# Expressions demonstrating operator precedence
expr1 = (a + b) * c          # Parentheses first
expr2 = a ** b + c           # Power first, then addition
expr3 = ~a + b               # NOT first, then addition
expr4 = a * b / c            # Multiply, then divide
expr5 = a + b - c            # Addition, then subtraction
expr6 = a < b and b > c      # Relational, then AND
expr7 = a | b and c          # AND, then OR

# Print results
print("Expression 1 ((a + b) * c):", expr1)  # Output: (5 + 2) * 3 = 21
print("Expression 2 (a ** b + c):", expr2)   # Output: 5**2 + 3 = 28
print("Expression 3 (~a + b):", expr3)       # Output: -6 + 2 = -4
print(f"Expression 4 (a * b / c): {expr4:.5f}")    # Output: 5 * 2 / 3 = 3.3333...
print("Expression 5 (a + b - c):", expr5)    # Output: 5 + 2 - 3 = 4
print("Expression 6 (a < b and b > c):", expr6)  # Output: False and True = False
print("Expression 7 (a | b and c):", expr7)      # Output: 5 | 2 = 7
