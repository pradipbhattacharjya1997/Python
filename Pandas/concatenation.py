import pandas as pd

df_Region1 = pd.DataFrame({
    'CustomerID':[1,2],
    'Name':['Gopal','Raju']
})
df_Region2 = pd.DataFrame({
    'CustomerID':[3,4],
    'Name':['Shyam','Baburao']
})

#concatenation vertically
df_concat =pd.concat([df_Region1,df_Region2], ignore_index=True)
print(df_concat)