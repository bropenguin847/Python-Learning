# greek_convert.py 
# Creating a conversion table as a dictionary 

greek_table = { 'alpha': '3B1', 'beta': '3B2', 'gamma': '3B3', 'delta': '3B4', 'epsilon': '3B5', 'zeta': '3B6', 'eta': '3B7', 'theta': '3B8' } 
# ^ Dictionary defininig each greek character
misc_table = { 'lesbian': '26A2', 'gay': '26A3', 'straight': '26A4', 'trans': '26A5',		 'trans2': '26A7', 'bjman': '13010', 'nsfw': '13072', 'nsfw2': '13055',
			  'skull': '2620', 'radioactive': '2622', 'communism': '262D', 'yin_yang': '262F', 'swastika': '5350'}

# Function to convert Greek letter names to their hex values 
def greek_to_hex(greek_name): 
	# Check if the Greek name is in the table 
	return greek_table.get(greek_name, 'Unknown') 
	# Returns 'Unknown' if the name is not found 

def unicode_xtended(self):
	x = misc_table.get(self, 'What are you 38 about bro?')
	return int(x,16)

def print_table():
      head = ["Name", "Code", "Symbol"]
      print(f"{head[0]:15} {head[1]:^10} {head[2]:^2}")
      for a, b in misc_table.items():
            symbol = chr(int(b, 16))
            print(f"{a:15} {b:^10} {symbol:^2}")
