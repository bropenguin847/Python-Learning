#Test 1 revision
#from array A, manipulate to get array B
# A = [[1,4,7],  
#      [2,5,8],
#      [3,6,9]]
# B = [[3 6 9 1
#       1 4 7 4
#       2 5 8 7]]

import numpy as np

A = np.array([[1, 4, 7],
              [2, 5, 8],
              [3, 6, 9]])

B = np.zeros([3,4])
row1 = np.insert(A[2], 3, A[0,0])
row2 = np.insert(A[0], 3, A[0,1])
row3 = np.insert(A[1], 3, A[0,2])

B = np.array([row1, row2, row3])
print(B)

#replace B's 0,0 with 4 and replace 2,3 with 9
B[0,0] = 4
B[2,3] = 9
print(B)

#replace entire first row with 8,8,8,8
B[0,:] = [8,8,8,8]
print(B)

#replace second column with 7,7,7
B[:,1] = [7,7,7]
print(B)

# Replace elements in Python row 1 and row 2, column 1 with [3, 6]
B[[1, 2], 1] = [3, 6]   #fancy ass indexing
print(B)

########################################################
a = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
b = np.array([[1, 0], [2, 1], [2, 1]])
X = a[[1, 2, 0]]    #is an array with size 3x3
Y = b[2]            #1d array
Z = b[[2]]          #2d array

a = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
b = np.array([a, 2*a])  #3D array
# b = [[[5, 10, 15],[20, 25, 30],[35, 40, 45]]  array b is 3d, with each layer being an array
#      [[10, 20, 30], [40,50,60],[70,80,90]]]
X = a[[1, 2, 0]]
Y = b[[1, 1, 0]]
Z = b[1, 1, 0]
#when printing Y, it will print out layers of array
#while print Z will output a single element

#chained comparison and order of precedence
x = (7 * 3) > 15 + 6 == 21
# x = 21 > 15 + 6 == 21
# x = 21 > 21 == 21
# x = False and True
# x = False

x = not ((4 * 4) >= 18 + 1 != 19)
# x = not(16 >= 18 + 1 != 19)
# x = not(16 >= 19 != 19)
# x = not(False and False)
# x = not(False)
# x = True

x = not (3 + (not 0) * 4 >= 18 - 2 != 16)
# x = not(3 + 1 * 4 >= 18 -2 != 16)
# x = not(3 + 4 >= 18 -2 != 16)
# x = not(7 >= 18 -2 != 16)
# x = not(7 >= 16 != 16)
# x = not(False and False)
# x = not(False)
# x = True

#converting for loop to while loop:
r = 0.08
a = np.array([100,500,800])
i = 0
while (i < len(a)):
    print(f"a = {a[i]}")
    j = 2
    while (j < 11):
        b = a[i] * (1 + r)**j
        print(f"b = {j} -> {b}")
        j += 2
    i += 1

#-----------using string methods--------------------------------------------
#Simulate a task management system where you can add, modify, remove, and organize tasks using Python list operations
# Step 1: Creating a list of tasks (strings)
tasks = ["Review project", "Email supervisor", "Schedule project meeting"]
print(f"\n\tThe initial tasks are as follows: {tasks}")

# Step 2: Accessing and displaying the first and last tasks
first_task = tasks[0]
last_task = tasks[-1]

# Step 3: Modifying a task in the list
tasks[1] = "Call project supervisor"
print(f"\tNow the changed tasks are: {tasks}")

# Step 4: Adding new tasks
# Adding a high-priority task at the beginning
tasks.insert(0, "Perform Kaizen on project")
# Adding multiple tasks at the end of the list
tasks.extend(["Eat breakfast", "Do warmup stretches", "check database"])
print(f"\tNow the new tasks are: {tasks}")

# Step 5: Removing tasks from the list
tasks.remove("Call supervisor")
print(f"\tAfter removing a task, now the updated tasks are : {tasks}")
# Removing the last task and displaying what was removed
removed_task = tasks.pop()
print("\tRemoved Task:", removed_task) 

# Step 6: Sorting tasks alphabetically
tasks.sort()
# Sorting tasks by length (shortest to longest)
tasks.sort(key=len)
print(f"\tsorted tasks are: {tasks}")

# Step 7: Using other string-specific methods
task_summary = ' | '.join(tasks)
print("Task Summary:", task_summary)
# Count occurrences of a specific word across tasks (e.g., "project")
project_count = sum(task.count("project") for task in tasks)
# Finding the index of a specific task
meeting_index = tasks.index("Eat breakfast")
