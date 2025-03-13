import pandas as pd

df = pd.read_json("/workspaces/Python/Pandas/sample_Data.json")

print('Displaying the info data set')
print(df.info())