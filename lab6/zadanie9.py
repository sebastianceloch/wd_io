import numpy as np
fib = np.empty((5,5), dtype='int')
a = 0
b = 1
for i in range(0,5,1):
    for j in range(0,5,1):
        fib[i,j]=b
        b += a
        a = b-a
print(fib)