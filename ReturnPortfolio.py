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
    