import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(1,20,20)
plt.plot(1/t,'g-->',label='f(x)=1/x')
plt.title('t/2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()