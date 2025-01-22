"""
Practice for question 4 in finals

Q4: Chapter 11 (Libraries: Numpy, Matplotlib & Pandas)
    Theory questions and write Python script for:
        - Creating dataframe
        - Missing data handling, remove and fill data
        - Outliers handling using IQR
"""


import os
import numpy as np
import pandas as pd
import matplotlib as plt

currrent_dir = os.path.dirname(__file__)
file_path = os.path.join(currrent_dir, "hello.csv")
# file_path = os.path.join(current_dir, ".xlsx")
df = pd.read_excel(file_path, sheet_name="")

# Declare important variables here
