'''
[“blue”, “green”, “red”, ”blue”, ”green”, “red”, ”blue”,”green”,”black”]
Complete all tasks below
1. Replace black with red
2. Insert white after every red
3. Sort Alphabetically
4. Delete all entry of green
''' 
colours = ["blue", "green", "red", "blue", "green", "red", "blue", "green", "black"]
print(colours)

# Since replace() is called onto the list, instead of the each element, let's change
#   each element in the list instead with a for loop
# Step 1
new_list = []   #make a new list first
for colour in colours:
    if colour == "black":
        colour = "red"
    new_list.append(colour)
colours = new_list
# Or the code belows works too
# for i in range(len(colours)):
#     if colours[i] == "black":
#         colours[i] = "red"
# Or
# colours = ["red" if color == "black" else color for color in colours]
print("\nstep 1 wowww")
print(colours)

# Step 2
for i in range(len(colours)):
    if colours[i] == "red":
        colours.insert(i+1, "white")
print("\nstep 2 yesss")
print(colours)

# Step 3
colours.sort()
print("\nstep 3 hell yea")
print(colours)

# Step 4
# Create a new list
new_list = []
for colour in colours:
    if colour != "green":
        new_list.append(colour)
colours = new_list
print("\nstep 4 finally")
print(colours)