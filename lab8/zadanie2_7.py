import pandas as pd 
import numpy as np 
import xlrd
import openpyxl
data = pd.ExcelFile('imiona.xlsx')
imiona = pd.read_excel('imiona.xlsx','Arkusz1')
dz = imiona[imiona['Plec'] == 'K']
dz_m = imiona[imiona['Plec'] == 'K'].max()
print(dz[(dz['Liczba'] == dz_m['Liczba'])])
ch = imiona[imiona['Plec'] == 'M']
ch_m = imiona[imiona['Plec'] == 'M'].max()
print(ch[(ch['Liczba'] == ch_m['Liczba'])])