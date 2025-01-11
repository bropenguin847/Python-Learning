"""
This is the file to use when playing around with codes from this chapter.
You can use this file to import functions that is in the same folder.
Use this file when you don't want to disturb the other codes and want to learn.

It is also fun to try :)
"""

import math

# Get user input for degree range and increment
degree_start = float(input('What starting value of degree would you like? '))
degree_final = float(input('What final value of degree would you like? '))
incr = float(input('What table increment would you like? '))

# Generate the degree list
degree = [i for i in range(int(degree_start), int(degree_final) + 1, int(incr))] 

# Calculate corresponding radians
radian = [deg / 180 for deg in degree] 

# Display the header
print('A table of degrees to radians')
print(' deg°        π rad')

# Print the table using formatted output and zip
for d, r in zip(degree, radian):  
    print(f'{d:6.2f}° {r:10.4f}π')
