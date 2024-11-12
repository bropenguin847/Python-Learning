import numpy as np

# a = np.array([100, 300, 500])
# b = np.array([0, 1, 2, 3, 4])
# c = np.zeros((3,5))
# for indexx, n in enumerate(b):
#     c[:, indexx] = a * n
# print(c)

x = np.array([[9, 8, 7, 6],
              [5, 4, 3, 2],
              [1, 0, 0, 2],
              [3, 4, 5, 6]])

y = np.array([[4, 0], [3, 0]])
z = np.array([[0],[1],[0],[1]])
a = np.array([[1],[2],[3],[4]])
b = np.array([[5, 10, 15, 20]])

c = x * a**2 * z + b
print(c)

a = np.array([100, 500, 800])
n = np.array([2, 4, 6, 8, 10])

N,A = np.meshgrid(n,a)
print(N)
print(A)