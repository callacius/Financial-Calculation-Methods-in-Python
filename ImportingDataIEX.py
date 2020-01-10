#!/usr/local/bin/python3
import numpy as np
import pandas as pd
from pandas_datareader import data as wb

PG = wb.DataReader('PG',data_source='iex',start='2015-1-1')

print(PG)