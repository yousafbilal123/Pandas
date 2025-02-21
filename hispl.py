import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('F:/1bbbbbbbbb/python pratice/pansdas/data.csv')
df["Duration"].plot(kind = 'hist')
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

