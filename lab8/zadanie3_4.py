import pandas as pd
import numpy as np 
import xlrd
import openpyxl
import datetime
z = pd.read_csv("zamowienia.csv",delimiter=";")
kraj = (z.groupby(['Kraj']).agg({"idZamowienia":['count']}))
print(kraj)