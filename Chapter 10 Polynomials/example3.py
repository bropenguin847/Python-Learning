import numpy as np

# Define the polynomials as vectors
p1 = [1, 3, 0, 2]  # Represents x^3 + 3x^2 + 2
p2 = [1, 0, -5]    # Represents x^2 - 5

# Polynomial multiplication to find f(x)
f_x = np.polymul(p1, p2)
print("f(x) (multiplication result) =", f_x)

# Polynomial division to find g(x)
g_x, remainder = np.polydiv(p1, p2)
print("g(x) (division result) =", g_x)
print("Remainder =", remainder)
