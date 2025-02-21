import pandas as pd

df = pd.read_csv('F:/1bbbbbbbbb/python pratice/pansdas/data.csv')

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

print(df.to_string())