#!/usr/local/bin/python3
import numpy as np
import pandas as pd
from pandas_datareader import data as wb

PG = wb.DataReader('PG',data_source='yahoo',start='1995-1-1')
print(PG)
# info - Informações sobre DataFrame(pandas)
print(PG.info())
# head - Mostra as 5 primeiros dados do DataFrame.
print(PG.head()) 
# tail - Mostra as 5 ultimos dados do DataFrame.
print(PG.tail())
# head - Passando a quantidade de retorno como parametro.
print(PG.head(20)) 
# tail - Passando a quantidade de retorno como parametro.
print(PG.tail(20))

tickers = ['PG','MSFT','T','F','G']
new_data = pd.DataFrame()
for t in tickers:
    new_data[t] = wb.DataReader(t,data_source='yahoo',start='1995-1-1')['Adj Close']
print(new_data.tail())