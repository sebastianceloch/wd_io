import pandas as pd
import numpy as np 
import xlrd
import openpyxl
import datetime
z = pd.read_csv("zamowienia.csv",delimiter=";")
nazwiska = z.Sprzedawca.unique()
print(nazwiska)