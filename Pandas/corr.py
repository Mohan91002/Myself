import os
import pandas as pd
import matplotlib.pyplot as plt
os.system("cls")

# df = pd.read_csv('dirtydata.csv')  
# print(df.corr())
# print()

# df = pd.read_csv('dirtydata.csv')
# df.plot()
# plt.show()
# print()

# df = pd.read_csv('dirtydata.csv')
# df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
# plt.show()
# print()

# df = pd.read_csv('dirtydata.csv')
# df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
# plt.show()
# print()

import sys
import matplotlib
matplotlib.use('Agg')
df = pd.read_csv('data.csv')
df["Duration"].plot(kind = 'hist')
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()