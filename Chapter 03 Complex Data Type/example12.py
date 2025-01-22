"""
Chapter 3 Example 12

Mixed Arithmetic, Relational, and Boolean Operations
"""

# Define sample variables
x = 8
y = 5
z = 12

# Combined operations
# This expression combines arithmetic, relational, and boolean logic
result = ((x + y) > z) and ((x - y) * 2 < z) or (z % y == 0)

# Explanation:
# - (x + y) > z checks if the sum of x and y is greater than z
# - ((x - y) * 2 < z) checks if double the difference between x and y is less than z
# - (z % y == 0) checks if z is divisible by y (no remainder)

# Display the result
print("Combined Result (integrating all operations):", result)  # Output will be a boolean value

# Additional mixed calculations
final_result = (x * y < z + 5) or ((x + 2) == (y + 5) and (z // y) > 1)

# Explanation:
# - (x * y < z + 5) checks if the product of x and y is less than z plus 5
# - ((x + 2) == (y + 5)) checks if x + 2 equals y + 5
# - (z // y) > 1 checks if the integer division of z by y is greater than 1

# Display the final result
print("Final Result (mixed operations):", final_result)  # Output will be a boolean value
