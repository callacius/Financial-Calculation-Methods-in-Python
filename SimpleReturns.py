##!/usr/local/bin/python3
import numpy as np 
from pandas_datareader import data as wb
import matplotlib.pyplot as plt 

PG = wb.DataReader('VALE3.SA',data_source='yahoo',start='1995-1-1')

print(PG.head())
print(PG.tail())

PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) - 1
print(PG['simple_return'])
# Retorno Simples(Uma ou várias ações)
PG['simple_return'].plot(figsize=(8,5))
#plt.show() Para exibirmos em um gráfico

# Taxa Média diária de retorno
# pandas.DataFrame.mean()
avg_returns_d = PG['simple_return'].mean()
print(avg_returns_d)

# Taxa Média Anual de Retorno
# pandas.DataFrame.mean() * 250(Dias de negociações por ano)
avg_returns_a = PG['simple_return'].mean() * 250
print(avg_returns_a)

# Para deixarmos mais apresentável
print(str(round(avg_returns_a, 5) * 100)+' %')


#plt.show()
