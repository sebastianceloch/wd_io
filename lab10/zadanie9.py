import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rd

df = pd.read_csv('zamowienia.csv',header=0,delimiter=';')
zm = df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
sprzedawca = df['Sprzedawca'].unique()
val = [int(zm.values[x]) for x in range(len(zm.values))]
Explode=[0 for i in range(len(zm.index.values))]
Explode[ val.index(max(val)) ]=0.1
ax = plt.subplot()
wedges,texts,autotexts = plt.pie(val, labels = sprzedawca, shadow = True,
                                explode = Explode,
                                startangle=45,
                                autopct=lambda pct: "{:.1f}%".format(pct), 
                                textprops=dict(color="black"))
ax.annotate('najlepszy sprzedawca',
            xy=(1,-0.5),
            xytext=(1.4,-0.8),
            arrowprops=dict(facecolor='black'))
plt.axis(xmax=2)
plt.title("Sumy zamowien sprzedawcow")
plt.legend(loc='upper right',title='sprzedawcy')
plt.show()