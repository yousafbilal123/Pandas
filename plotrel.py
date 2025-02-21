import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('F:/1bbbbbbbbb/python pratice/pansdas/data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

plt.show()