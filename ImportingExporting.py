#!/usr/local/bin/python3
import quandl

quandl.ApiConfig.api_key = 'tEsTkEy123456789'
quandl.ApiConfig.api_version = '2015-04-09'
quandl.ApiConfig.verify_ssl = False

mydata_01 = quandl.get("FRED/GDP")
mydata_01.tail()