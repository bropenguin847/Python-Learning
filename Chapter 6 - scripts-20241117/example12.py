# Writing binary data to a file 
with open('binaryfile.bin', 'wb') as file: 	file.write(b'\x01\x02\x03')

# Reading binary data from a file 
with open('binaryfile.bin', 'rb') as file: 
	binary_content = 	file.read() 	
	print(binary_content) 
