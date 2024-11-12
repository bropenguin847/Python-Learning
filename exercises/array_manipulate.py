#from array A, manipulate to get array B
# A = [[1,4,7],  
#      [2,5,8],
#      [3,6,9]]
# B = [[3 6 9 1
#       1 4 7 4
#       2 5 8 7]]
import numpy as np

A = np.array([  [1,4,7],
                [2,5,8],
                [3,6,9]])

#3 methods: np.insert, np.take, np.hstack

#Method 1:  syntax is np.insert(arr, obj, values)
row1 = np.insert(A[2], 3, A[0, 0])
row2 = np.insert(A[0], 3, A[0, 1])
row3 = np.insert(A[1], 3, A[0, 2])
B = np.array([row1, row2, row3])
print(B)

#Method 2: use np.take
row1 = np.take(A, [6,7,8,0])
row2 = np.take(A, [0,1,2,1])
row3 = np.take(A, [3,4,5,2])
B = np.array([row1, row2, row3])
print(B)

#Method 3: use np.hstack
row1 = np.hstack([A[2,:], A[0,0]])
row2 = np.hstack([A[0,:], A[0,1]])
row3 = np.hstack([A[1,:], A[0,2]])
B = np.array([row1, row2, row3])
print(B)