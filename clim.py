import pandas as pd

df = pd.read_csv('F:/1bbbbbbbbb/python pratice/pansdas/data.csv')

df["Calories"].fillna(130, inplace = True)