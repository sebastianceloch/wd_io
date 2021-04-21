import numpy as np
def diag(x):
    v=[]
    for n in range(x,0,-1):
        v.append(n)
    d = np.diag([v for v in range(x,0,-1)])
    return d
print(diag(5))
