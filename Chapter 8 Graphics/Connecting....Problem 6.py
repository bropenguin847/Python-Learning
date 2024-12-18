import numpy as np 
import matplotlib.pyplot as plt 

mean = 70
std_dev = 10
num_of_students = 1000
test_scores = np.random.normal(mean, std_dev, num_of_students)

#Histogram
plt.hist(test_scores, bins=20)
plt.title("Histogram of Student's Test Scores")
plt.xlabel('Test Scores')
plt.ylabel("Numbers of students")
plt.grid(True)
plt.show()