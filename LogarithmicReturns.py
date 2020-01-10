#!/usr/local/bin/python3
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

PG = wb.DataReader('PG',data_source='yahoo',start='1995-1-1')

print(PG.head())
print(PG.tail())

PG['log_return'] = np.log(PG['Adj Close'] / PG['Adj Close'].shift(1))
print (PG['log_return'])
# Retorno Logarítmico(uma única ação)
PG['log_return'].plot(figsize=(8, 5))
plt.show()

# Taxa Média diária de retorno
# pandas.DataFrame.mean()
log_return_d = PG['log_return'].mean()
print(log_return_d)

# Taxa Média Anual de Retorno
# pandas.DataFrame.mean() * 250(Dias de negociações por ano)
log_return_a = PG['log_return'].mean() * 250
print(log_return_a)

# Para deixarmos mais apresentável
print (str(round(log_return_a, 5) * 100) + ' %')