import pandas as pd
import numpy as np

s = pd.Series([1,3,5,np.nan,6,8])
print(s)

s = pd.Series([10,12,8,14], index=['Ala','Marek','WWiesiek','Elenorno'])
print(s)

data = {'Kraj': ['Belgia', 'Indie','Brazylia'],
'Stolica':['Bruksela','new delhi','brasilia'],
'Populacjha':[11151,12311,515311]}
df = pd.DataFrame(data,columns=['Kraj','Stolica','Populacjha'])
print(df)

daty = pd.date_range('20210428',periods=5)
print(daty)
df = pd.DataFrame(np.random.randn(5,4), index=daty, columns=list('ABCD'))
print(df)

