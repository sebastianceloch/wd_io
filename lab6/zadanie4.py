import numpy as np, math as m
def potegowanie(n,k):
    tab = np.logspace(1,k,num=k,base=n,dtype='int')
    return tab
print(potegowanie(2,4))