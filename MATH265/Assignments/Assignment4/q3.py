import matplotlib.pyplot as plt
import math
import matplotlib as mpl
import numpy as np
import sympy
from sympy.abc import x


x1 = np.arange(-10,10,0.01)   # start,stop,step
y1 = sympy.sympify(((x**2)-4)/((x**2)+6))
y1 = sympy.lambdify(x, y1, 'numpy')

plt.grid(True)
plt.axhline(y=0, lw=1, color='black')
plt.axvline(x=0, lw=1, color='black')
plt.xticks(np.arange(-100, 100, 1.0))
plt.yticks(np.arange(-100, 100, 1.0))


plt.plot(x1,y1(x1), color='black', linewidth=1)

plt.ylim(-10, 10)
plt.xlim(-10, 10)
# plt.plot(3, 9, marker='.', color='black')

plt.show()
