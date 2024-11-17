import numpy as np

degree_start = float(input("What starting value of degree: "))
degree_final = float(input("What final value of degree: "))
incr = float(input("What table increment: "))

degree = [i for i in range(int(degree_start), int(degree_final) + 1, int(incr))]
radian = [deg / 180 for deg in degree]
print('A table of degrees to radians')
print(f' deg° π rad')
for d, r in zip(degree, radian):
    print(f'{d:6.2f}° {r:10.4f}π')

A[:,2], A[0:1,0:1]