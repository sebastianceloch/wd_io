import pandas as pn
import xlrd
import openpyxl
df = pn.read_excel('imiona.xlsx')
suma = df['Liczba'].sum()
print(suma)