"""
A custom library to be used in main.py

A conversiob table is created as a dictionary
"""

greek_table = {'alpha': '3B1', 'beta': '3B2', 'gamma': '3B3', 'delta': '3B4',
               'epsilon': '3B5', 'zeta': '3B6', 'eta': '3B7', 'theta': '3B8' } 
# ^ Dictionary defininig each greek character

misc_table = {'lesbian': '26A2', 'gay': '26A3', 'straight': '26A4', 'trans': '26A5',
              'trans2': '26A7', 'bjman': '13010', 'nsfw': '13072', 'nsfw2': '13055',
            'skull': '2620', 'radioactive': '2622', 'communism': '262D', 'yin_yang':
            '262F', 'swastika': '5350'}

def greek_to_hex(greek_name):
    """
    Takes in the greek letter and return the hex values
    Check if the Greek name is in the table
    Returns 'Unknown' if the name is not found
    """
    return greek_table.get(greek_name, 'Unknown')

def unicode_xtended(self):
    """
    Gets misc letter and returns the hex values
    """
    x = misc_table.get(self, 'Try again please?')
    return int(x,16)

def print_table():
    """
    Prints a table of name, code and symbol
    with predefined sizes
    """
    head = ["Name", "Code", "Symbol"]
    print(f"{head[0]:15} {head[1]:^10} {head[2]:^2}")
    for a, b in misc_table.items():
        symbol = chr(int(b, 16))
        print(f"{a:15} {b:^10} {symbol:^2}")
