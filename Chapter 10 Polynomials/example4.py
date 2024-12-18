import numpy as np

# Set P, D, and I values (Proportional, Derivative, Integral gains)
P, D, I = 4, 2, 1

# Motor's transfer function H(s) = 1/(s - 2)
H_n = [1]  # Motor's numerator (constant)
H_d = [1, -2]  # Motor's denominator (s - 2)

# Controller's numerator and denominator (PID controller)
G_n = [D, P, I]  # D s^2 + P s + I
G_d = [1, 0]  # Denominator (s for 1/s term)

# System's numerator Q_n = G_n * H_n, denominator Q_d = G_d * H_d
Q_n = np.polymul(G_n, H_n)
Q_d = np.polymul(G_d, H_d)

# Output result
print("Numerator Q_n:", Q_n)  # [2, 4, 1] -> 2s^2 + 4s + 1
print("Denominator Q_d:", Q_d)  # [1, -2, 0] -> s^2 - 2s
