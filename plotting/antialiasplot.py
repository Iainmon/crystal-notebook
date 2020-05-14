import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LinearLocator, FormatStrFormatter


# def get_demo_image():
#     from matplotlib.cbook import get_sample_data
#     import numpy as np
#     f = get_sample_data("axes_grid/bivariate_normal.npy", asfileobj=False)
#     z = np.load(f)
#     # z is a numpy array of 15x15
#     return z, (-3, 4, -4, 3)

# fig, ax = plt.subplots(figsize=[5, 4])

# # make data
# Z, extent = get_demo_image()
# Z2 = np.zeros([150, 150], dtype="d")
# ny, nx = Z.shape
# Z2[30:30 + ny, 30:30 + nx] = Z

# ax.imshow(Z2, extent=extent, interpolation="nearest",
#           origin="lower")

# # inset axes....
# axins = ax.inset_axes([0.5, 0.5, 0.47, 0.47])
# axins.imshow(Z2, extent=extent, interpolation="nearest",
#           origin="lower")
# # sub region of the original image
# x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9
# axins.set_xlim(x1, x2)
# axins.set_ylim(y1, y2)
# axins.set_xticklabels('')
# axins.set_yticklabels('')

# ax.indicate_inset_zoom(axins)

# plt.show()




img = mpimg.imread('./images/rough_shape.png')
# plt.imshow(img)
# # lum_img = img[:, :, 0]
# # plt.imshow(lum_img)
# plt.show()




# img = mpimg.imread('./images/rough_shape.png')
img = mpimg.imread('./images/smooth_shape.png')

# plt.imshow(img)

fig, ax = plt.subplots()

# make data
lum_img = img[:, :, 0]
Z = img
extent = (-1, 1, -1, 1)
Z2 = np.zeros([500, 500, 4], dtype="d")
# Z2 = np.zeros([530, 530], dtype="d")
# ny, nx = Z.shape
ny, nx = 500, 500
Z2[0:0 + ny, 0:0 + nx] = Z

ax.imshow(Z2, extent=extent, interpolation="nearest",
          origin="lower")

ax.set_xticklabels('')
ax.set_yticklabels('')

# inset axes....
axins = ax.inset_axes([0.5, 0.5, 0.5, 0.5])
axins.imshow(Z2, extent=extent, interpolation="nearest",
          origin="lower")
# sub region of the original image
x1, x2, y1, y2 = -.6, -.4, -.6, -.4
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
axins.set_xticklabels('')
axins.set_yticklabels('')

ax.indicate_inset_zoom(axins)
plt.tight_layout()
plt.show()







# fig, ax = plt.subplots() # create a new figure with a default 111 subplot
# ax.imshow(img)
# from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
# axins = zoomed_inset_axes(ax, 2.5, loc=2) # zoom-factor: 2.5, location: upper-left
# axins.plot(img)

# x1, x2, y1, y2 = 47, 60, 3.7, 4.6 # specify the limits
# axins.set_xlim(x1, x2) # apply the x-limits
# axins.set_ylim(y1, y2) # apply the y-limits
# plt.yticks(visible=False)
# plt.xticks(visible=False)
# from mpl_toolkits.axes_grid1.inset_locator import mark_inset
# mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")










# from scipy import ndimage, misc
# import matplotlib.pyplot as plt

# fig = plt.figure()
# ax1 = fig.add_subplot(121)  # left side
# ax2 = fig.add_subplot(122)  # right side
# ascent = misc.ascent()
# result = ndimage.zoom(ascent, 10.0)
# ax1.imshow(ascent)
# result = result[30:30 + 500, 30:30 + 500]
# ax2.imshow(result)
# plt.show()
