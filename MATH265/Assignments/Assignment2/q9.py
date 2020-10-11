import matplotlib.pyplot as plt
import math
import matplotlib as mpl
import numpy as np

x1 = np.arange(-4.999,0,0.001)   # start,stop,step
y1 = (-1/x1)+5.8

x2 = np.arange(0.01,5.01,0.001)   # start,stop,step
y2 = (6/5)*x2

x3 = np.arange(5,15.01,0.01)   # start,stop,step
y3 = -x3+11

plt.grid(True)
plt.axhline(y=0, lw=1, color='black')
plt.axvline(x=0, lw=1, color='black')
plt.xticks(np.arange(-20, 20, 1.0))
plt.yticks(np.arange(-20, 20, 1.0))


plt.plot(x1,y1, color='black', linewidth=1)
plt.plot(x2,y2, color='black', linewidth=1)
plt.plot(x3,y3, color='black', linewidth=1)

plt.plot(5, 6, marker='.', color='black')
plt.plot(-5, 6, marker='.', color='black')
plt.plot(0, 0, marker='o', color='black', fillstyle = 'none')

plt.arrow(5, 6, 10, -10, head_width=0.5, head_length=0.75, fc='k', ec='k')

plt.show()