import numpy as np

def potegi(n):
    diag = np.diag([2 for _ in range(n)])
    for i in range(1, n):
        v = [2+(2*i) for _ in range(n-i)]
        diag += np.diag(v, i)
        diag += np.diag(v, -i)
    return diag

print(potegi(3))