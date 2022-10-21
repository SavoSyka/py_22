import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

f=np.exp
min_x=0
max_x=20
N=100
min_y=1
max_y=100000

plt.ylim(min_y,max_y)
plt.xlim(min_x,max_x)

plt.grid('True')
plt.yscale('log')
x = np.linspace(min_x,max_x,N)
y = f(x)
plt.plot(x,y,'g-.')
plt.show()
plt.savefig("function.png")