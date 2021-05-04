import pandas as pd
import numpy as np 
import xlrd
import openpyxl
import datetime
z = pd.read_csv("zamowienia.csv",delimiter=";")
max=z.sort_values('Utarg',ascending=False)
print(max.iloc[:5])