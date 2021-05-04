import pandas as pd
import xlrd
import openpyxl
df = pd.read_excel('imiona.xlsx')
d = df[df['Liczba']>1000]
print(d)