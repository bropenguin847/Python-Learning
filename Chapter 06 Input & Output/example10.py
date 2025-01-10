"""
Chapter 6 Example 10
"""

# Writing to a text file
with open('example.txt', 'w') as file:
    file.write('Hello, World!')

# Reading from a text file 
with open('example.txt', 'r') as file:
    content = file.read()
    print(content) # Output: Hello, World!

# Writing binary data to a file
with open('binaryfile.bin', 'wb') as file:
    file.write(b'\x01\x02\x03')

# Reading binary data from a file 
with open('binaryfile.bin', 'rb') as file:
    binary_content = file.read()
    print(binary_content)
