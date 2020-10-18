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
plt.xticks(np.arange(-100, 100, 0.1))
plt.yticks(np.arange(-100, 100, 1))

plot_x1 = x1
plot_y1 = y1(x1)
plot_y2 = y2(x1)
plot_y3 = y3(x1)

plt.plot(plot_x1,plot_y1, color='black', linewidth=1)
plt.plot(plot_x1,plot_y2, color='black', linewidth=1)
plt.plot(plot_x1,plot_y3, color='black', linewidth=1)

# plt.plot(3, 9, marker='.', color='black')

# from stackoverflow question https://stackoverflow.com/questions/16417496/matplotlib-fill-between-multiple-lines

section = np.arange(0, 0.52, 0.01)
y_area = np.minimum(y1(section), y3(section)) # top two line bounds

plt.ylim(0, 20)
plt.xlim(-1, 1)

plt.fill_between(section, y2(section), y_area) # y2 is the bottom line bound

plt.text(0.5, 4.2, "a (0.5, 4)")
plt.text(0.05, 0, "b (0, 0)")
plt.text(0.25, 16, "c (0.25, 16)")

plt.show()