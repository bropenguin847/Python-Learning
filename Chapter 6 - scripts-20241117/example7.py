import math 
# Define the values for w and s similar to MATLAB 
w = [0, math.pi/2, math.pi, 3*math.pi/2] 
s = [math.sin(wi) for wi in w] # Calculate sine values 
omega = '\u03C9' # Unicode representation for omega 

# Print the formatted header line using f-strings 
print(f'{omega} sin({omega})')

# Print each value of w and s with formatted output using f-strings print(f'{w[0]/math.pi:1.1f}\u03C0 {s[0]:10.3f}') 
print(f'{w[1]/math.pi:1.1f}\u03C0 {s[1]:10.3f}') 
print(f'{w[2]/math.pi:1.1f}\u03C0 {s[2]:10.3f}') 
print(f'{w[3]/math.pi:1.1f}\u03C0 {s[3]:10.3f}')
