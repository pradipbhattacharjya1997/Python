##adding columns
import pandas as pd

data = {
    "Name":['Ram','shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,4500,52000,49000,70000,48000,58000],
    "Performancce Score":[85,90,78,92,88,95,80,89]

}

df = pd.DataFrame(data)

#square brakcets df["Column_name"]=some_Data
print(df)

df["Bonus"] = df['Salary'] * 0.1
print(df)

#using insert()
#df.insert(loc, "Column_name",some_data)

df.insert(0,"Employee ID", [10,20,30,40,50,60,70,80])
print(df)