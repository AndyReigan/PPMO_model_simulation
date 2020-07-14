from mpl_toolkits.
import matplotlib.pyplot as plt

map = Basemap(projection='ortho', lat_0=50, lon_0=-100, resolution='l', area_thresh=1000.0)
map.drawcoastlines()
plt.show()