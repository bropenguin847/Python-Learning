import matplotlib.pyplot as plt
import numpy as np

# Step 1: 2D line plot
t= np.arange(0, 61, 1)
A=np.sin(0.1*np.pi*t)

plt.plot(t, A)
plt.xlabel("Seismic amplitude A(t)")
plt.ylabel("Time(t)")
plt.title("Seismic amplitude A(t) over time(t)")
plt.show()

# Step 2: Stem plot
t= np.arange(0, 61, 1)
A=np.sin(0.1*np.pi*t)

plt.stem(t, A)
plt.xlabel("Seismic amplitude A(t)")
plt.ylabel("Time(t)")
plt.title("Seismic amplitude A(t) over time(t)")
plt.show()

# Step 3: Normal plot vs log-log plot
EE=[10**n for n in range(1,11,1)] 
t=np.arange(1,11,1)
plt.subplot(1, 2, 1)
plt.plot(t,EE)
plt.xlabel("Time (t)")
plt.ylabel("Energy Released (EE)/j")
plt.title("Energy released(EE)/j over time(t)")

plt.subplot(1, 3, 3)
plt.loglog(t,EE)
plt.xlabel("Time (log t)")
plt.ylabel("Energy Released (log EE)")
plt.title("Energy released (log EE) over time(log t)")

plt.show()

# Step 4: Log-log plot
LL=[30, 35, 50, 40, 45, 55,50, 60, 65, 70, 75, 80, 85, 90, 95, 100, 95, 85, 80, 75, 70, 65, 60, 55]
t=np.arange(1,25,1)
plt.loglog(t,LL)
plt.xlabel("Time (log t)")
plt.ylabel("Sound Intensity (log LL)")
plt.title("Sound Intensity (log LL) over Time (log t))")

plt.show()

# Step 5: Bode plot
R=10000
C=1e-6
f=np.arange(1,10001,1000)
H = 1/(1 + 1j *2*np.pi* f * R * C)

magnitude=(20*np.log10(np.abs(H)))
phase = np.angle(H) 

#Magnitude plot
plt.subplot(2, 1, 1)
plt.semilogx(f, magnitude)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.title("Magnitude(dB) over freqyency(Hz)")


#Phase plot
plt.subplot(2, 1, 2) 
plt.semilogx(f, phase/np.pi)
plt.xlabel("Frequency, f (Hz)")
plt.ylabel("Phase (π rad)") 
plt.yticks(np.arange(-1, 1.5, 0.5), [f'{tick:.1f}π' for tick in np.arange(-1, 1.5, 0.5)])
plt.title("Phase (π rad) over frequency(Hz)")
plt.tight_layout()
plt.show() 

# Step 6: Histogram
mean = 4
std_dev = 0.5
num_of_earthquake = 100
test_scores = np.random.normal(mean, std_dev, num_of_earthquake)

plt.hist(test_scores, bins=10)
plt.title("Histogram of magnitude distribution")
plt.xlabel("Magnitude distribution(M)")
plt.ylabel("Numbers of earthquake")
plt.show()

# Step 7: Box plot
mean_north= 10
std_dev_north=2
mean_south=12
std_dev_south=3
num_of_earthquake=100

north=np.random.normal(mean_north, std_dev_north, num_of_earthquake)
south=np.random.normal(mean_south, std_dev_south, num_of_earthquake)

data=[north,south]

plt.figure()
plt.boxplot(data,labels=["North","South"])
plt.title("Box plot of North and South sensor measurement(X)")
plt.ylabel("Sensor measurement (X)")
plt.show()








