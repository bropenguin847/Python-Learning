import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d

A = np.matrix([[2, 3],
               [5, 6]])

B = np.matrix([[8, 9],
               [2,1]])

left_div = np.linalg.solve(A, B)
right_div = np.linalg.solve(A.T, B.T).T

nums1 = [1, 2, 3, 4, 5]
nums2 = [3, 4, 5, 6, 7]
result = []
for i, j in zip(nums1, nums2):
    result.append(i * j)
print(result)

custom_num = [324324,2342,6574, 5765 ,23542 ,2342]
for index, num in enumerate(custom_num):
    print(index, num)