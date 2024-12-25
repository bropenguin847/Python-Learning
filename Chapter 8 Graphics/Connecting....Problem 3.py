
#Problem 3
import matplotlib.pyplot as plt
import numpy as np
A = 5
ω= 2
#Displacement x(t)

#x-axis
t=np.arange(0, 11, 1)
#y-axis
x= A * np.sin(ω*t)  

plt.subplot(1,2,1)
plt.plot(t,x)
plt.title("Displacement x(t)")
plt.xlabel("Time(t)")
plt.ylabel("Displacement(x)")
           
#Velocity v(t)

#x-axis
t=np.arange(0, 11, 1)
#y-axis
v= A * ω * np.cos(ω*t)  

plt.subplot(1,2,2)
plt.plot(t,v)
plt.title("Velocity v(t)")
plt.xlabel("Time(t)")
plt.ylabel("Velocity(v)")

plt.show()