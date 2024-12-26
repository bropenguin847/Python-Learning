# Writing to a text file 
with open('example.txt', 'w') as file: 
	file.write('Hello, World!') 

# Reading from a text file 
with open('example.txt', 'r') as file: 
	content = file.read() 
	print(content) # Output: Hello, World!

	