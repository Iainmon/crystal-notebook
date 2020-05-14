from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import cm
import matplotlib
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

def clamp(n, smallest, largest): return max(smallest, min(n, largest))

def hr(a, b, phi):
    t = (phi - a) / (b - a)
    # phi = clamp(t, a, b)
    phi = np.vectorize(clamp)(t, 0, 1)
    return (-2*(phi**3)) + (3*(phi**2))


color_scheme = "viridis" # viridis, inferno, plasma, jet, magma

hermite_interpolation_latex = r'$hr_a^b\left(\phi\right)$'

# rc('font', **{'family': 'CMU Classical Serif', 'style': 'italic'})
plt.rcParams['mathtext.fontset'] = 'cm'
# rc('mathtext.default', **{'family': 'CMU Classical Serif', 'style': 'italic'})
# plt.style.use('ggplot')




# Make data.
X = np.arange(-1, 1, 0.05)
Y = np.arange(-1, 1, 0.05)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = R # np.sin(R)





#
# Interpolated heatmap plot
#

# b = 0
# sharpness = 1
# #Z = hr(b, b + (1 / sharpness), Z)

# plt.figure()
# plt.title(r'$color = hue(z)$', fontsize=14)

# p = plt.imshow(Z, cmap=color_scheme, interpolation="bilinear", extent=[-1,1,-1,1])
# # p = plt.pcolormesh(X,Y,Z, cmap="viridis")

# p.axes.xaxis.set_major_locator(LinearLocator(5))
# p.axes.set_xlabel(r'$x$', fontsize=14)
# p.axes.yaxis.set_major_locator(LinearLocator(5))
# p.axes.set_ylabel(r'$y$', fontsize=14, rotation=0)

# plt.colorbar(p)
# # plt.colorbar(p, extend="both")
# # plt.clim(0,np.sqrt(2))

# plt.show()

# exit(0)



#
# 3d Plot
#
# fig = plt.figure()
# # ax = fig.gca(projection='3d')
# ax = fig.add_subplot(111, projection='3d')

# # Plot the surface.
# surf = ax.plot_surface(X, Y, Z, cmap=color_scheme, rstride=1, cstride=1, edgecolor='none',
#                        linewidth=10, antialiased=True)

# # rc('font', **{'family': 'CMU Serif', 'style': 'italic'})

# # Costomize the axeye.
# ax.set_xlim(-1,1)
# ax.xaxis.set_major_locator(LinearLocator(5))
# ax.set_xlabel(r'$x$', fontsize=14)

# ax.set_ylim(-1,1)
# ax.yaxis.set_major_locator(LinearLocator(5))
# ax.set_ylabel(r'$y$', fontsize=14)

# ax.set_zlim(0, 1)
# ax.zaxis.set_major_locator(LinearLocator(3))
# ax.set_zlabel(r'$z$', fontsize=14)
# # ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# # Add a color bar which maps values to colors.
# # fig.colorbar(surf, shrink=1, aspect=5)
# fig.colorbar(surf)

# # plt.title(r'$f(x,y)$', fontsize=14)
# # plt.title(r'$f\left(x,y\right)=\sqrt{x^2+y^2}$', fontsize=14)
# # plt.title(hermite_interpolation_latex, fontsize=14)
# plt.show()



#
# Heatmap plot
#
#
# plt.figure()
# plt.title(r'$color = hue(z)$', fontsize=14)
# p = plt.imshow(Z, cmap=color_scheme, interpolation="bilinear", extent=[-1,1,-1,1])
# # p = plt.pcolormesh(X,Y,Z, cmap="viridis")

# p.axes.xaxis.set_major_locator(LinearLocator(5))
# p.axes.set_xlabel(r'$x$', fontsize=14)
# p.axes.yaxis.set_major_locator(LinearLocator(5))
# p.axes.set_ylabel(r'$y$', fontsize=14, rotation=0)

# plt.colorbar(p)
# # plt.colorbar(p, extend="both")
# # plt.clim(0,np.sqrt(2))

# plt.show()



#
# UV Offset plots
#

# font_size = 16

# X = np.arange(0, 1, 0.02)
# Y = np.arange(0, 1, 0.02)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = R # np.sin(R)

# plt.figure()
# # plt.title(r'$f\left(\vec{uv\:}\right)$', fontsize=14)
# plt.title(r'$f\left(\vec{uv \:}\right)$', fontsize=font_size)
# p = plt.imshow(Z, cmap=color_scheme, interpolation="bilinear", extent=[0,1.,0,1], origin="lower")
# # p = plt.pcolormesh(X,Y,Z, cmap="viridis")

# p.axes.xaxis.set_major_locator(LinearLocator(3))
# p.axes.set_xlabel(r'$\vec{uv \:}_x$', fontsize=font_size)
# # p.axes.set_xlabel(r'$x$', fontsize=14)
# p.axes.yaxis.set_major_locator(LinearLocator(3))
# p.axes.set_ylabel(r'$\vec{uv \:}_y$', fontsize=font_size, rotation=0)
# # p.axes.set_ylabel(r'$y$', fontsize=14, rotation=0)

# plt.colorbar(p)
# # plt.colorbar(p, extend="both")
# # plt.clim(0,np.sqrt(2))

# plt.show()

# X = np.arange(-.5, .5, 0.02)
# Y = np.arange(-.5, .5, 0.02)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = R # np.sin(R)

# plt.figure()
# # plt.title(r'$f\left(\vec{uv\:}\right)$', fontsize=14)
# plt.title(r'$f\left(\vec{\sigma}\right)$', fontsize=font_size)
# p = plt.imshow(Z, cmap=color_scheme, interpolation="bilinear", extent=[-.5,.5,-.5,.5], origin="lower")
# # p = plt.pcolormesh(X,Y,Z, cmap="viridis")

# p.axes.xaxis.set_major_locator(LinearLocator(3))
# p.axes.set_xlabel(r'$\vec{\sigma}_x$', fontsize=font_size)
# # p.axes.set_xlabel(r'$x$', fontsize=14)
# p.axes.yaxis.set_major_locator(LinearLocator(3))
# p.axes.set_ylabel(r'$\vec{\sigma}_y$', fontsize=font_size, rotation=0)
# # p.axes.set_ylabel(r'$y$', fontsize=14, rotation=0)

# plt.colorbar(p)
# # plt.colorbar(p, extend="both")
# # plt.clim(0,np.sqrt(2))

# plt.show()


#
# 3d plot plane clipping/slicing
#

# fig = plt.figure()
# ax = fig.gca(projection='3d')

# # X = np.arange(-1, 1, 0.05)
# # Y = np.arange(-1, 1, 0.05)
# # X, Y = np.meshgrid(X, Y)

# Z1 = np.empty_like(X)
# Z2 = np.empty_like(X)
# C1 = np.empty_like(X, dtype=object)
# C2 = np.empty_like(X, dtype=object)

# for i in range(len(X)):
#   for j in range(len(X[0])):
#     z1 = np.sqrt(X[i,j]**2+Y[i,j]**2)
#     z2 = .6
#     Z1[i,j] = z1
#     Z2[i,j] = z2

#     # If you want to grab a colour from a matplotlib cmap function, 
#     # you need to give it a number between 0 and 1. z1 and z2 are 
#     # already in this range, so it just works as is.
#     norm = matplotlib.colors.Normalize(vmin=0, vmax=np.sqrt(2))
#     C1[i,j] = plt.get_cmap(color_scheme)(norm(z1))
#     C2[i,j] = plt.get_cmap("Oranges")(norm(1))


# # Create a transparent bridge region
# X_bridge = np.vstack([X[-1,:],X[-1,:]])
# Y_bridge = np.vstack([Y[-1,:],Y[-1,:]])
# Z_bridge = np.vstack([Z1[-1,:],Z2[-1,:]])
# color_bridge = np.empty_like(Z_bridge, dtype=object)

# color_bridge.fill((1,1,1,0)) # RGBA colour, onlt the last component matters - it represents the alpha / opacity.

# # Join the two surfaces flipping one of them (using also the bridge)
# X_full = np.vstack([X, X_bridge, np.flipud(X)])
# Y_full = np.vstack([Y, Y_bridge, np.flipud(Y)])
# Z_full = np.vstack([Z1, Z_bridge, np.flipud(Z2)])
# color_full = np.vstack([C1, color_bridge, np.flipud(C2)])

# surf_full = ax.plot_surface(X_full, Y_full, Z_full, rstride=1, cstride=1,
#                             facecolors=color_full, linewidth=0,
#                             antialiased=True, edgecolor="none")

# ax.set_xlim(-1,1)
# ax.xaxis.set_major_locator(LinearLocator(5))
# ax.set_xlabel(r'$x$', fontsize=14)

# ax.set_ylim(-1,1)
# ax.yaxis.set_major_locator(LinearLocator(5))
# ax.set_ylabel(r'$y$', fontsize=14)

# ax.set_zlim(0, 1)
# ax.zaxis.set_major_locator(LinearLocator(3))
# ax.set_zlabel(r'$z$', fontsize=14)

# ax.text(-1,-1,.68, r'$r$', fontsize=14)

# fig.colorbar(surf)

# plt.show()


density = 500

x = np.arange(-1,1,1/(density/2))
r1 = np.empty(density)
r1.fill(.4)
r2 = np.empty(density)
r2.fill(.46)
y2 = np.concatenate((np.arange(0,1,1/(density/2)) , np.arange(1,0,-(1/(density/2)))), axis=None) # np.array([0, .5, 1, .5, 0])
y = np.maximum(r1, y2)
print(len(r2))
fig = plt.figure()
ax = plt.gca()

# ax.set_title('interpolation=True')
ax.plot(x, r1, '--')
ax.plot(x, r2, '--')
ax.plot(x, y2)
ax.fill_between(x, y, r2, where=(y < r2), color='C1', alpha=0.3,
                 interpolate=True)
# ax.fill_between(x, y2, r2, where=(r1 < y2), color='C0', alpha=0.3,
#                 interpolate=True)
# ax.fill_between(x, y1, y2, where=(y1 <= y2), color='C1', alpha=0.3,
#                  interpolate=True)
# fig.tight_layout()

plt.show()