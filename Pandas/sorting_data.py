#sorting data
#Sorting data 1 column sort_values()
# df.sort_values(by="Column Name", True/False, inplace = True)

import pandas as pd

data = {
    "Name":['Arun','Varun','karun'],
    "Age":[28,34,22],
    "Salary":[10000,20000,30000]
}

df=pd.DataFrame(data)
print(df)

df.sort_values(by=['Age',"Salary"],ascending=[True, False], inplace = True)
print('Sorted Age by Descending')
print(df)