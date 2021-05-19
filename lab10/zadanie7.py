import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

x = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel('imiona.xlsx','Arkusz1')
ch = df[df['Plec']=='M'].groupby(['Rok']).agg({'Liczba':['sum']})
d = df[df['Plec']=='K'].groupby(['Rok']).agg({'Liczba':['sum']})
lata = df['Rok'].unique()
wch = [int(ch.values[x]) for x in range(len(ch))]
wd = [int(d.values[x]) for x in range(len(d))]
plt.bar(lata,wch, color='red', label = 'chlopcy')
plt.bar(lata,wd, color='blue', label = 'dziewczyny', bottom = wch)
plt.legend(loc='upper right')
plt.xlabel('Rok')
plt.xticks(lata ,rotation=90)
plt.show()