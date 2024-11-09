# Title Classification #
import numpy as np
    
name_list = []
age_list = []
cgpa_list = []
title_list = []

def classify(cgpa):
    if cgpa >= 3.69:
        return "1st Class"
    elif cgpa >= 3.50:
        return "Dean's List"
    elif cgpa >= 3.00:
        return "2nd Class"
    elif cgpa >= 2.00:
        return "3rd Class"
    else:
        return "Fail"

n_students  = int(input("How many students: "))
for i in range (0,n_students):
    print("\nStudent info ", i + 1, ":")
    name = input("Student name: ")
    name_list.append(name)  #add the name input into the list

    age = input("Student age: ")
    age_list.append(age)    #add the age into the list

    cgpa = float(input("Student CGPA: "))
    cgpa_list.append(cgpa)
    title = classify(cgpa)
    title_list.append(title)    #add title to the list

print("------------")
final_list = np.concatenate([[name_list],[age_list],[cgpa_list], [title_list]])
total_rows = len(final_list)
total_columns = len(final_list[0])
print(final_list)

#------------------------------------------------------------------
# from tkinter import *
# window = Tk()
# window.title("Title Classification")
# window.geometry('600x500')
# t = Table(window)
# window.mainloop()
# add main function
#------------------------------------------------------------------