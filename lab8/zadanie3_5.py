import pandas as pd
import numpy as np 
import xlrd
import openpyxl
import datetime
z = pd.read_csv("zamowienia.csv",delimiter=";")
sum=z[(z['Data zamowienia']>='2005-01-01')&(z['Data zamowienia']<='2005-12-31')& (z['Kraj']=='Polska')]
sum.groupby(['Kraj']).count
print(sum['idZamowienia'])