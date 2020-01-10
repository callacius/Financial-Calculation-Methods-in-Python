##!/usr/local/bin/python3
import numpy as np
import pandas as pd 
from pandas_datareader import data as wb
import matplotlib.pyplot as plt 

tickers = ['PG','MSFT','F','GE']

mydata = pd.DataFrame()
for t in tickers:
    mydata[t] = wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']

mydata.info()
print(mydata.head())
print(mydata.tail())

#  Normalizar para 100, Igualar o inicio para ficar mais apresentável
#  no grafico

mydata.iloc[0]
(mydata/mydata.iloc[0] * 100).plot(figsize = (15,6));
print(plt.show())
mydata.loc['1995-01-03'] 
mydata.iloc[0]

# Calcular o Retorno simples das acões
returns = (mydata / mydata.shift(1)) -1
print(returns.head())

weights = np.array([0.25,0.25,0.25,0.25])
np.dot(returns,weights)

annual_returns = returns.mean() * 250
print(annual_returns)

np.dot(annual_returns,weights)
pfolio_1 = str(round(np.dot(annual_returns,weights),5)*100)+' %'


weights_2 = np.array([0.4,0.4,0.15,0.05])
pfolio_2 = str(round(np.dot(annual_returns,weights_2),5)*100)+' %'

print(pfolio_1)
print(pfolio_2)

