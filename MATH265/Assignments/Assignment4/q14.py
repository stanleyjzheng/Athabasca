import matplotlib.pyplot as plt
import math
import matplotlib as mpl
import numpy as np
import sympy
from sympy.abc import x
from sympy import sin, cos, pi


x1 = np.arange(-10,10,0.01)   # start,stop,step
y1 = sympy.sympify(1/(x**2))
y1 = sympy.lambdify(x, y1, 'numpy')

y2 = sympy.sympify(8*x)
y2 = sympy.lambdify(x, y2, 'numpy')

y3 = sympy.sympify(64*x)
y3 = sympy.lambdify(x, y3, 'numpy')

plt.grid(True)
plt.axhline(y=0, lw=1, color='black')
plt.axvline(x=0, lw=1, color='black')
plt.xticks(np.arange(-10, 10, 1.0))
plt.yticks(np.arange(-10, 10, 1.0))

plot_x1 = x1
plot_y1 = y1(x1)
plot_y2 = y2(x1)
plot_y3 = y3(x1)

plt.plot(plot_x1,plot_y1, color='black', linewidth=1)
plt.plot(plot_x1,plot_y2, color='black', linewidth=1)
plt.plot(plot_x1,plot_y3, color='black', linewidth=1)

# plt.plot(3, 9, marker='.', color='black')

section = np.arange(0, 10, 0.01)
#y_area = np.minimum(y1(section), y2(section))
y_area = np.minimum(np.minimum(y1(section), y2(section)), y3(section))


plt.ylim(0, 5)

plt.fill_between(section, y1(section), y_area)

plt.show()