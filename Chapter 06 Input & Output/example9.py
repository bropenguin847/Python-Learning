"""
Chapter 6 Example 9
This example uses pickle
"""

import pickle

# Saving an object to a binary file
data = {'key': 'value', 'bit': 'byte'}
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Loading an object from a binary file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    print(loaded_data) # Output: {'key': 'value'}
