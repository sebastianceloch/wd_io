import pandas as pd 
import numpy as np
import xlrd
import openpyxl
data = pd.ExcelFile('imiona.xlsx')
imiona = pd.read_excel('imiona.xlsx','Arkusz1')
p = imiona.sort_values("Liczba", ascending=False).groupby(['Rok',"Plec"]) 

for x,y in enumerate(p,start=1):
    print(f"{y[0]}")
    print(f"{y[1].iloc[[0],[1]].values[0][0]}", end=" ")
    print(f"{y[1].iloc[[0],[2]].values[0][0]}")
