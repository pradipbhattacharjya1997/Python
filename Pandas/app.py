import pandas as pd


# read data from CSV file into a dataframe
df = pd.read_csv("/workspaces/Python/Pandas/sales_data_sample.csv",encoding="latin1")
print(df)

#read data from JSON file into a dataframe
# df = pd.read_json("/workspaces/Python/Pandas/sample_Data.json")
# print(df)

# #read data from xlsx file into a dataframe
# df = pd.read_excel("/workspaces/Python/Pandas/SampleSuperstore.xlsx")
# print(df)