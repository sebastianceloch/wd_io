import pandas as pn  
import numpy as np
import xlrd
import openpyxl
df = pn.read_excel('imiona.xlsx')
d =df.groupby(by=['Rok']).sum()
sum=df['Liczba'][(df['Rok']<=2005) & (df['Rok']>=2000)].sum()
print(sum)