import pandas as pd

df = pd.read_csv('F:/1bbbbbbbbb/python pratice/pansdas/data.csv')

df.dropna(inplace = True)

print(df.to_string())