import pandas as pd
import numpy as np

df = pd.read_csv("Updated_Shoes.csv")

list1 = []

for i in range(len(df)):
    if df.at[i, 'no_of_ratings'] is not np.NaN:
        d = df.at[i, 'no_of_ratings']
        a = ''
        if ',' in d:
            for j in d:
                a += ''.join(j) if j != ',' else ''
            list1.append(a)
        else:
            list1.append(d)
    else:
        list1.append(df.at[i, 'no_of_ratings'])

df["no_of_ratings"] = list1

print(df.to_string())
df.to_csv("Updated_Shoes.csv")

"""
list1 = []

for i in range(len(df)):
    if df.at[i, 'actual_price'] is not np.NaN:
        list1.append(df.at[i, 'actual_price'][1:])
    else:
        list1.append(df.at[i, 'actual_price'])

df['actual_price'] = list1

print(df.to_string())
df.to_csv("Updated_Shoes.cssv")
"""
