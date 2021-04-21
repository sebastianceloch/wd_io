import numpy as np
def tablice(n):
    zera = np.zeros((n,n))
    g=0
    for x in range(n):
        for j in range(n):
            zera[x][j]=g
            g+=1
    return zera  
print(tablice(4)) 