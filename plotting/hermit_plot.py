import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from matplotlib.ticker import LinearLocator, FormatStrFormatter

plt.rcParams['mathtext.fontset'] = 'cm'
# plt.rc('axes', titlesize=20)
# plt.rc('axes', labelsize=14)

# plt.rc('font', size=14)

def clamp(n, smallest, largest): return max(smallest, min(n, largest))

def hr(a, b, phi):
    # phi = np.vectorize(clamp)(phi, a, b)
    # phi = np.vectorize(clamp)((phi - a) / (b - a), 0, 1)
    phi = clamp((phi - a) / (b - a), 0, 1)
    return (-2*(phi**3)) + (3*(phi**2))


# Data for plotting
x = np.arange(0.0, 1.0, 0.001)

# f = 1 + np.sin(2 * np.pi * x)
f = np.arange(0.0, 1.0, 0.001)


a = .3
b = .8

for y in range(len(f)):
    f[y] = hr(a, b, f[y])


fig, ax = plt.subplots()
ax.plot(x, f)

p1 = np.arange(0.0, 1.0, 0.001)
p1.fill(a)
p2 = np.arange(0.0, 1.0, 0.001)
p2.fill(b)

fontsize = 16

ax.plot(p1, x, '--')
ax.annotate(r'$a=.3$', xy=(a+.01,.2), fontsize=fontsize)

ax.plot(p2, x, '--')
ax.annotate(r'$b=.8$', xy=(b+.01, .2), fontsize=fontsize)


ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

ax.xaxis.set_major_locator(LinearLocator(3))
ax.yaxis.set_major_locator(LinearLocator(3))

ax.set_xlabel(r'$x$', fontsize=fontsize)
ax.set_ylabel(r'$y$', fontsize=fontsize, rotation=0)
ax.grid()

plt.show()