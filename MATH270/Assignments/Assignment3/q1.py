import matplotlib.pyplot as plt
import math
import matplotlib as mpl
import numpy as np

#Q1A (f(x))

# x1 = np.arange(-15,-2.001,0.001)   # start,stop,step
# y1 = 4+0*x1

# x2 = np.arange(-2,3.01,0.001)   # start,stop,step
# y2 = x2**2

# x3 = np.arange(3,20,0.001)   # start,stop,step
# y3 = 2/(x3-3)

# plt.grid(True)
# plt.axhline(y=0, lw=1, color='black')
# plt.axvline(x=0, lw=1, color='black')
# plt.xticks(np.arange(-20, 20, 1.0))
# plt.yticks(np.arange(-20, 20, 1.0))


# plt.plot(x1,y1, color='black', linewidth=1)
# plt.plot(x2,y2, color='black', linewidth=1)
# plt.plot(x3,y3, color='black', linewidth=1)

# plt.plot(3, 9, marker='.', color='black')

# plt.show()


#Q1B (f'(x))

x1 = np.arange(-15,-2.001,0.001)   # start,stop,step
y1 = 0+0*x1

x2 = np.arange(-2,3.01,0.001)   # start,stop,step
y2 = 2*x2

x3 = np.arange(3,20,0.001)   # start,stop,step
y3 = 2/(x3-3)

plt.grid(True)
plt.axhline(y=0, lw=1, color='black')
plt.axvline(x=0, lw=1, color='black')
plt.xticks(np.arange(-20, 20, 1.0))
plt.yticks(np.arange(-20, 20, 1.0))


plt.plot(x1,y1, color='black', linewidth=1)
plt.plot(x2,y2, color='black', linewidth=1)
plt.plot(x3,y3, color='black', linewidth=1)

plt.plot(3, 9, marker='.', color='black')

plt.show()