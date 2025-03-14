""""df["Column Name"].mean()
df["Column Name"].Sum()
df["Column Name"].min()
df["Column Name"].max()
"""

import pandas as pd

data = {
     "Name":['Arun','Varun','karun'],
    "Age":[28,34,22],
    "Salary":[10000,20000,30000]
}

df =pd.DataFrame(data)

#avg_salary
avg_salary = df['Salary'].mean()
print(avg_salary)

#max_age
max_age = df['Age'].max()
print(max_age)