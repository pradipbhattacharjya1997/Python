#pd.merge(df1,df2, on="Column_Name",how="type of join")

import pandas as pd

#customer dataframe

df_customers = pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':['Ramesh','Suresh','Kalpesh']
})

#order dataframe
df_orders = pd.DataFrame({
    'CustomerID':[1,2,4],
    'OrderAmount':[250,450,350]
})

#merge
df_merged =pd.merge(df_customers,df_orders,on="CustomerID", how="outer")
print('outer join')
print(df_merged)