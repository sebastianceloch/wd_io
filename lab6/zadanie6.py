import numpy as np
w = 'wiersz'
k = 'kolumna'
c = 'kloc'
n = 8
wykres = np.empty((n, n), dtype='str')

for i in range(0, n, 1):
    for j in range(0, n, 1):
        wykres[i, j] = ' '

for i in range(0, len(k), 1):
    wykres[i+1, 0] = k[i]

for i in range(0, len(w), 1):
    wykres[0, i+1] = w[i]

for i in range(0, len(c), 1):
    wykres[i, i] = c[i]

for i in range(0, n, 1):
    for j in range(0, n, 1):
        print(wykres[i, j],'', end='')
    print()