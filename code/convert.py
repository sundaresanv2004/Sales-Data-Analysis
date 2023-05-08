import pandas as pd
import numpy as np

df = pd.read_csv("Shoes.csv")

list1 = []

for i in range(len(df)):
    if df.at[i, 'discount_price'] is not np.NaN:
        list1.append(df.at[i, 'discount_price'][1:])
    else:
        list1.append(df.at[i, 'discount_price'])

df['discount_price'] = list1

print(df.to_string())
