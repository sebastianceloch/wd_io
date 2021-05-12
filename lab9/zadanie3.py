import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

dane = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(dane)

uro = df[((df.Rok <= 2017) & (df.Rok >= 2013))]
uro = uro.groupby("Plec")["Liczba"].sum()
wykres = uro.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
plt.title("Procent urodzonych chłopcow i dziewczynek w ostatnich 5 latach")
plt.show()