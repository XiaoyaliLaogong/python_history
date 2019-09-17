import pandas as pd
import tushare as ts
import matplotlib.pyplot as plt
import numpy as np
df = ts.get_hist_data('002583')
df.to_csv('data.csv')

datahigh = df['high'].values
datalow = df['low'].values

dataclose = df['close'].values

datamid = np.add(datahigh, datalow)


datamid = np.divide(datamid, 2)
#datamid = np.min(datamid,dataclose)
datam = datamid-dataclose
'''
plt.plot(df['open'])
plt.plot(df['high'])
plt.plot(df['low'])
plt.plot(df['close'])
plt.show()

'''
print('datam:\n{0}'.format(df))
plt.plot(df['volume'].values)
plt.plot(df['close'].values)

plt.show()