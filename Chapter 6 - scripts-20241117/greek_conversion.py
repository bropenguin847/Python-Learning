# greek_conversion.py 
# Creating a conversion table as a dictionary 

greek_table = { 'alpha': '3B1', 'beta': '3B2', 'gamma': '3B3', 'delta': '3B4', 'epsilon': '3B5', 'zeta': '3B6', 'eta': '3B7', 'theta': '3B8' } 

# Function to convert Greek letter names to their hex values 
def greek_to_hex(greek_name): 
	# Check if the Greek name is in the table 
	return greek_table.get(greek_name, 'Unknown') 
	# Returns 'Unknown' if the name is not found 



