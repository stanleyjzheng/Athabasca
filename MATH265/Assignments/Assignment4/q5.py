import matplotlib.pyplot as plt
import math
import matplotlib as mpl
import numpy as np
import sympy
from sympy.abc import x
from sympy import sin, cos, pi


x1 = np.arange(-10,10,0.01)   # start,stop,step
y1 = sympy.sympify(sin(x))
y1 = sympy.lambdify(x, y1, 'numpy')

y2 = sympy.sympify(x**2)
y2 = sympy.lambdify(x, y2, 'numpy')

plt.grid(True)
plt.axhline(y=0, lw=1, color='black')
plt.axvline(x=0, lw=1, color='black')
plt.xticks(np.arange(-10, 10, 1.0))
plt.yticks(np.arange(-10, 10, 1.0))

plot_x1 = x1
plot_y1 = y1(x1)
plot_y2 = y2(x1)

plt.plot(plot_x1,plot_y1, color='black', linewidth=1)
plt.plot(plot_x1,plot_y2, color='black', linewidth=1)

idx = np.argwhere(np.diff(np.sign(plot_y1 - plot_y2))).flatten()
plt.plot(plot_x1[idx], plot_y1[idx], 'ro')

for i in idx:
    plt.text(plot_x1[i], plot_y1[i], f'({"%.2f" % plot_x1[i]}, {"%.2f" % plot_y1[i]})')

# plt.plot(3, 9, marker='.', color='black')

plt.show()