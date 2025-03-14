import pandas as pd

data = {
    "Name":['Arun','Varun','Karun','Narun','Marun'],
    "Age":[28,34,22,34,28],
    "Salary":[50000,60000,45000,54000,480000]
}

df =pd.DataFrame(data)
print(df)

grouped =df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)
