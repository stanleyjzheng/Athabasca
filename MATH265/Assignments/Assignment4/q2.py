import matplotlib.pyplot as plt
import math
import matplotlib as mpl
import numpy as np
import sympy
from sympy.abc import x
from sympy import sin, cos, pi


x1 = np.arange(-10,9,0.01)   # start,stop,step
y1 = sympy.sympify(-(x**3)/(x-9))
y1 = sympy.lambdify(x, y1, 'numpy')

x2 = np.arange(4,10,0.01)
y2 = sympy.sympify(-1/(x-4)+2)
y2 = sympy.lambdify(x, y2, 'numpy')

plt.grid(True)
plt.axhline(y=0, lw=1, color='black')
plt.axvline(x=0, lw=1, color='black')
plt.xticks(np.arange(-100, 100, 1))
plt.yticks(np.arange(-100, 100, 1))

plot_y1 = y1(x1)
plot_y2 = y2(x2)

plt.plot(x1,plot_y1, color='black', linewidth=1)
plt.plot(x2,plot_y2, color='black', linewidth=1)


plt.ylim(-10, 10)
plt.xlim(-10, 10)

plt.show()