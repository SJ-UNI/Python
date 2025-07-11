from mpl_toolkits.basemap import basemap
import matplotlib.pyplot as plt
map = basemap(resolution='l')
map.drawmapboundary(fill_color="blue")
map.fillcontinents(color="green")
map.drawcoastlines()
