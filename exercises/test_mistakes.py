"""
Mistakes made in my test that made me question life
"""
import numpy as np

a = np.array([1, 2])
b = np.array([[1,2],[3,4]])
c = a*b.T
print(c)

"""
Since a is only [1, 2] in order to multiply b [[1, 2], [3, 4]]
a needs to be broadcasted to [[1, 2], [1, 2]] in order to perform the element wise multiply
"""

a = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
b = np.array([a, 2*a])
X = a[[1, 2, 0]]
Y = b[[1, 1, 0]]    # There is difference between double bracket and single bracket
Z = b[1, 1, 0]      # For single bracket it is just basic indexing, fancy indexing uses double bracket.  

"""
I had made the mistake of thinking that single bracket is fancy indexing, thus getting out
can you imagine my pain when i made this mistake, even though i had read about it???!!!
it hurts more when you know the concept already, but you still make the mistake, than when you dont know
    the mistake
"""