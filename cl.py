import pandas as pd

df = pd.read_csv('F:/1bbbbbbbbb/python pratice/pansdas/data.csv')

new_df = df.dropna()

print(new_df.to_string())