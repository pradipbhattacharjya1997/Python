"""
1-how big is your dataset
2- what are the name of columns

shape and columns
"""

import pandas as pd

data = {
    "Name":['Ram','shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,4500,52000,49000,70000,48000,58000],
    "Performancce Score":[85,90,78,92,88,95,80,89]

}

df =pd.DataFrame(data)
print(df)
print(f'Shape: {df.shape}')
print(f'Column Names: {df.columns}')