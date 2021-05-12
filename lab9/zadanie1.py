import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

dane = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(dane)

uro = df.groupby("Rok")["Liczba"].sum()
wykres = uro.plot(color="r")
wykres.set_ylabel('Liczba urodzen')
plt.title("Wykres urodzonych dzieci dla kazdego roku")
plt.show()