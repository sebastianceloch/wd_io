import pandas as pd
import numpy as np 
import xlrd
import openpyxl
import datetime
z = pd.read_csv("zamowienia.csv",delimiter=";")
sr = z[(z['Data zamowienia'] >= '2004-01-01') & (z['Data zamowienia'] <= '2004-12-31')].mean()
print(sr['Utarg'])