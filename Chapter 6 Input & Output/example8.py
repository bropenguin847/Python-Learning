import math 
# Define the values for w and s similar to MATLAB 
w = [0, math.pi/2, math.pi, 3*math.pi/2] 
s = [math.sin(wi) for wi in w] # Calculate sine values 
omega = '\u03C9' # Unicode representation for omega 

# Print the formatted header line using f-strings 
print(f'{omega} sin({omega})') 

# Use a for loop to print each value of w and s 
for i in range(len(w)): 
	print(f'{w[i]/math.pi:1.1f}\u03C0 {s[i]:10.3f}')
