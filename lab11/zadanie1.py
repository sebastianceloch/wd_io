import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math as m 
fig = plt.figure()
ax = fig.gca(projection = '3d')
n = np.arange(0,2*np.pi,0.1)
t = n
x = np.sin(n)
y = np.cos(n)*2
ax.plot(x,y,t,label = 'sinx i 2*cosx')
ax.legend()
plt.show()
