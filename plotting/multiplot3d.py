from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erf

fig = plt.figure()
ax = fig.gca(projection='3d')

X = np.arange(0, 6, 0.05)
Y = np.arange(0, 6, 0.05)
X, Y = np.meshgrid(X, Y)

Z1 = np.empty_like(X)
Z2 = np.empty_like(X)
C1 = np.empty_like(X, dtype=object)
C2 = np.empty_like(X, dtype=object)

for i in range(len(X)):
  for j in range(len(X[0])):
    z1 = 0.5*(erf((X[i,j]+Y[i,j]-4.5)*0.5)+1)
    z2 = 0.5*(erf((-X[i,j]-Y[i,j]+4.5)*0.5)+1)
    Z1[i,j] = z1
    Z2[i,j] = z2

    # If you want to grab a colour from a matplotlib cmap function, 
    # you need to give it a number between 0 and 1. z1 and z2 are 
    # already in this range, so it just works as is.
    C1[i,j] = plt.get_cmap("Oranges")(z1)
    C2[i,j] = plt.get_cmap("Blues")(z2)


# Create a transparent bridge region
X_bridge = np.vstack([X[-1,:],X[-1,:]])
Y_bridge = np.vstack([Y[-1,:],Y[-1,:]])
Z_bridge = np.vstack([Z1[-1,:],Z2[-1,:]])
color_bridge = np.empty_like(Z_bridge, dtype=object)

color_bridge.fill((1,1,1,0)) # RGBA colour, onlt the last component matters - it represents the alpha / opacity.

# Join the two surfaces flipping one of them (using also the bridge)
X_full = np.vstack([X, X_bridge, np.flipud(X)])
Y_full = np.vstack([Y, Y_bridge, np.flipud(Y)])
Z_full = np.vstack([Z1, Z_bridge, np.flipud(Z2)])
color_full = np.vstack([C1, color_bridge, np.flipud(C2)])

surf_full = ax.plot_surface(X_full, Y_full, Z_full, rstride=1, cstride=1,
                            facecolors=color_full, linewidth=0,
                            antialiased=False)

plt.show()




# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# import numpy as np

# fig = plt.figure()
# ax = fig.gca(projection='3d')
# X = np.arange(-5, 5, 0.05)
# Y = np.arange(-5, 5, 0.05)
# X, Y = np.meshgrid(X, Y)

# # Complex shape from examples in matplotlib gallery
# Z1 = np.sin(np.sqrt(X**2+Y**2))
# Z2 = np.ones_like(Z1)*0.6

# # Define the color for each one of our surfaces
# # (it doesn't need to be a gradient)
# color1 = np.empty_like(X, dtype=str)
# color1.fill('b')
# color2 = np.empty_like(X, dtype=str)
# color2.fill('r')

# # Create a white bridge region
# X_bridge = np.vstack([X[-1,:],X[0,:]])
# Y_bridge = np.vstack([Y[-1,:],Y[0,:]])
# Z_bridge = np.vstack([Z1[-1,:],Z2[0,:]])
# color_bridge = np.empty_like(Z_bridge, dtype=object)
# color_bridge.fill((1,1,1,0))

# # Join the two surfaces (using also the bridge)
# X_full = np.vstack([X, X_bridge, X])
# Y_full = np.vstack([Y, Y_bridge, Y])
# Z_full = np.vstack([Z1, Z_bridge, Z2])
# color_full = np.vstack([color1, color_bridge, color2])

# surf_full = ax.plot_surface(X_full, Y_full, Z_full, rstride=1, cstride=1,
#                                     facecolors=color_full, linewidth=0,
#                                                                 antialiased=False)

# ax.set_zlim3d(-1, 2)
# ax.set_ylim(-5,5)
# ax.set_xlim(-5,5)

# plt.show()