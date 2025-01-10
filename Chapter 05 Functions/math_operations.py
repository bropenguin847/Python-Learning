"""
This module defines basic mathematical operations.
"""

def add(a, b):
    """
    Returns the sum of two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Returns the difference between two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The difference between a and b (a - b).
    """
    return a - b

def multiply(a, b):
    """
    Returns the product of two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Returns the quotient of two numbers.

    Args:
        a (int or float): The numerator.
        b (int or float): The denominator.

    Raises:
        ZeroDivisionError: If b is zero.

    Returns:
        float: The quotient of a and b (a / b).
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

def power(a, b):
    """
    Returns the result of a raised to the power of b.

    Args:
        a (int or float): The base.
        b (int or float): The exponent.

    Returns:
        int or float: The result of a raised to the power of b (a^b).
    """
    return a ** b

def factorial(n):
    """
    Returns the factorial of a non-negative integer.

    Args:
        n (int): The non-negative integer.

    Raises:
        ValueError: If n is negative.

    Returns:
        int: The factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
