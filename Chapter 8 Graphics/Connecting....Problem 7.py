import numpy as np 
import matplotlib.pyplot as plt 

mean_height_teamA= 180
std_dev_height_teamA= 6
mean_height_teamB= 190
std_dev_height_teamB= 6
num_of_players=50

height_teamA=np.random.normal(mean_height_teamA, std_dev_height_teamA, num_of_players)
height_teamB=np.random.normal(mean_height_teamB, std_dev_height_teamB, num_of_players)

height_data=[height_teamA,height_teamB]
#box plot
plt.figure()
plt.boxplot(height_data,labels=["TeamA","TeamB"])
plt.title("Box plot of basketball players's height")
plt.ylabel("Height(cm)")
plt.show()

