import pandas as pd

df = pd.read_csv('F:/1bbbbbbbbb/python pratice/pansdas/data.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())