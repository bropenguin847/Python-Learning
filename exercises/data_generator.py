"""
Generates data-filled csv files
3 columns, 50 rows
field	:		age 	    height	        bank acc
			    1 - 90	    40 - 200	    0 - 100_000
uses random
"""

import random
import numpy as np
import pandas as pd

age = []
height = []
bank_acc = np.zeros(50, dtype=float)

for i in range(50):
    age.append(random.randint(1, 90))
    height.append(random.randint(40, 200))
    bank_acc[i] = round(random.uniform(0, 100_000), 2)

# Adding Nan values into Bank Acc
bank_acc[(bank_acc < 100_000) & (bank_acc > 80_000)] = np.nan

df = pd.DataFrame({
    'Age': age,
    'Height': height,
    'Bank Acc': bank_acc
})

# Convert dataframe to csv file
df.to_csv('random_data.csv', index=False)
