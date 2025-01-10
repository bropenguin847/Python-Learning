"""
Example 5: Lambda Functions

A lambda function is a small, anonymous function defined in a single line.
It is often used for short, simple operations where defining a full function
using def might be overkill.

Basic Syntax:
    lambda arguments: expression

arguments: A comma-separated list of arguments the function takes.
expression: A single expression that the function evaluates and returns.

Key Points:

Lambda are often used with higher-order functions like map(), filter(), and reduce().
They can make your code more concise and readable in some cases.
However, for complex operations, it's generally better to use
regular functions defined with def.
"""

square = lambda x: x ** 2
print(square(4)) # Output: 16

addition = lambda a, b: a + b
print(addition(3, 5))
