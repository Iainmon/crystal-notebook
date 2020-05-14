from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# plt.style.use('bmh')
plt.rcParams['mathtext.fontset'] = 'cm'

domain = (-1, 1, .05)

z = np.array([[ np.sqrt(x**2 + y**2) for x in np.arange(*domain)] for y in np.arange(*domain)])
x, y = np.meshgrid(range(z.shape[0]), range(z.shape[1]))

color_scheme = "inferno"

# show hight map in 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z,
                cmap=color_scheme,
                rstride=1, cstride=1,
                edgecolor='none',
                linewidth=10, antialiased=True)

# ax.set_xlim(-1, 1)
# ax.set_ylim(-1, 1)

plt.title(r'$z = f(x,y)$', fontsize=14)
plt.show()

# show hight map in 2d
plt.figure()
plt.title(r'$color = hue(z)$', fontsize=14)
p = plt.imshow(z, cmap=color_scheme, interpolation="bilinear")
plt.colorbar(p)
plt.show()