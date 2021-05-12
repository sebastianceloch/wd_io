import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

dane = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(dane)

uro = df.groupby("Plec")["Liczba"].sum()
wykres = uro.plot.bar()
wykres.set_ylabel('Liczba urodzen')
wykres.set_xlabel('plec')
plt.title("Liczba urodzonych chłopcow i dziewczynek")
plt.show()