from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

# rc('font', **{'family': 'CMU Classical Serif', 'style': 'italic'})
plt.rcParams['mathtext.fontset'] = 'cm'
# rc('mathtext.default', **{'family': 'CMU Classical Serif', 'style': 'italic'})
# plt.style.use('ggplot')

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-1, 1, 0.05)
Y = np.arange(-1, 1, 0.05)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)# + noise.pnoise2(X, Y)
Z = R # np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap="viridis", rstride=1, cstride=1, edgecolor='none',
                       linewidth=10, antialiased=True)

# rc('font', **{'family': 'CMU Serif', 'style': 'italic'})

# Costomize the axeye.
ax.set_xlim(-1,1)
ax.xaxis.set_major_locator(LinearLocator(3))
ax.set_xlabel(r'$x$', fontsize=14)

ax.set_ylim(-1,1)
ax.yaxis.set_major_locator(LinearLocator(3))
ax.set_ylabel(r'$y$', fontsize=14)

ax.set_zlim(0, 1)
ax.zaxis.set_major_locator(LinearLocator(3))
ax.set_zlabel(r'$z$', fontsize=14)
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=1, aspect=5)

plt.title(r'$f(x,y)$', fontsize=14)
plt.show()

plt.figure()
plt.title(r'$color = hue(z)$', fontsize=14)
p = plt.imshow(Z, cmap="viridis", interpolation="bilinear", extent=[-1,1,-1,1])
p.axes.xaxis.set_major_locator(LinearLocator(5))
p.axes.yaxis.set_major_locator(LinearLocator(5))
# p = plt.pcolormesh(X,Y,Z, cmap="viridis")
plt.colorbar(p)
plt.show()