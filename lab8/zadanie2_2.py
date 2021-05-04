import pandas as pd
import xlrd
import openpyxl
df = pd.read_excel('imiona.xlsx')
szukaj = df[df.Imie == 'SEBASTIAN']
print(szukaj)