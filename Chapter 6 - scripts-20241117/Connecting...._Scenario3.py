# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 21:46:11 2024

@author: ASUS
"""

import pandas as pd

def adjust_price (category,price):
    if category == "Electronics":
        return price*1.1
    elif category == "Clothing":
        return price*0.95
    else:
        return price

  
df = pd.read_excel('product_catalog.xlsx', sheet_name='Products')

data = df.to_numpy()

adjusted_price=[]
stock=[]

for i in range(len(data)):
    adjusted_price.append(adjust_price(data[i,2],data[i,3])) 
    if data[i,4] >0:
        stock.append("In Stock")
    else:
        stock.append("Out of stock")
   
df['Adjusted price']=adjusted_price
df['In/Out of stock']=stock

with pd.ExcelWriter('product_catalog.xlsx', mode='a', if_sheet_exists='overlay') as writer:
    df.to_excel(writer, sheet_name='Products', index=False, header=True)