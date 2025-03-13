import pandas as pd

data = {
    "Name":['Ram','shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,4500,52000,49000,70000,48000,58000],
    "Performancce_Score":[85,90,78,92,88,95,80,89]

}

df =pd.DataFrame(data)
print(df)

#df.drop(columns = ["ColumnName"],inplace=True)
print("Modified Data")
df.drop(columns=["Performancce_Score","Age"],inplace=True)
print(df)