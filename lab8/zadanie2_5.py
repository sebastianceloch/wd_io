import pandas as pn  
import numpy as np
import xlrd
import openpyxl
df = pn.read_excel('imiona.xlsx')
suma = df.groupby(by=['Plec']).sum()
print(suma['Liczba'])