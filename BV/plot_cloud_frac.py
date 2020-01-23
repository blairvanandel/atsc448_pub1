from pyhdf.SD import SD, SDC

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm
import calendar
import pprint


# all code below taken from MIT (https://www.science-emergence.com/Codes/Plot-MODIS-C6-MYD06-Cloud-Fraction-with-python/)

#----------------------------------------------------------------------------------------#
# Inputs

#file_name = './inputs/myd06_granules_viz/MYD06_L2.A2008015.1435.006.2013342100940.hdf'

#----------------------------------------------------------------------------------------#
# Extract Year, Month, Day, Hour and Minutes from file name


def cloud_frac_plot(file_name):
	path = file_name.split('/')
	name = path[len(path)-1]
	list = name.split('.')

	hhmm = list[2]
	hh = int(hhmm[0:2])
	mm = int(hhmm[2:4])

	year = int(list[1][1:5])
	dayofyear = int(list[1][5:8])

	month = 1
	day = dayofyear
	while day - calendar.monthrange(year,month)[1] > 0 and month <= 12:
		day = day - calendar.monthrange(year,month)[1]
		month = month + 1

	#print year, month, day, hh, mm

	#----------------------------------------------------------------------------------------#
	# Read HDF Files

	file = SD(file_name, SDC.READ)

	data_selected_id = file.select('Cloud_Fraction')

	data = data_selected_id.get()

	data_selected_attributes = data_selected_id.attributes()

	#pprint.pprint( data_selected_attributes )

	scale_factor = data_selected_attributes['scale_factor']
	add_offset = data_selected_attributes['add_offset']

	#----------------------------------------------------------------------------------------#
	# Plot data

	data = data * scale_factor

	data_shape = data.shape

	cmap = [(0.0,0.0,0.0)] + [(cm.jet(i)) for i in range(256)]
	cmap = mpl.colors.ListedColormap(cmap)

	bounds = [0.0, 0.1, 0.2 , 0.3 , 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

	norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

	fix, ax = plt.subplots(figsize=(10,10))
	ax.imshow(np.fliplr(data), cmap=cmap, norm=norm,
	                  interpolation='none', origin='lower')

	cbar_bounds = [0.0, 0.1, 0.2 , 0.3 , 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
	cbar_ticks = [0.0, 0.1, 0.2 , 0.3 , 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

	#cbar = plt.colorbar(ax, cmap=cmap, norm=norm, boundaries=cbar_bounds, ticks=cbar_ticks)
	#cbar.ax.set_yticklabels(cbar_ticks, fontsize=10)

	l = [int(i) for i in np.linspace(0,data_shape[1],6)]
	#plt.xticks(l, [i for i in reversed(l)], rotation=0, fontsize=8 )

	l = [int(i) for i in np.linspace(0,data_shape[0],9)]
	#plt.yticks(l, l, rotation=0, fontsize=8 )

	title = 'Cloud Fraction \n MYD06 C6 ({}-{:02d}-{:02d}; {:02d}h{:02d})'

	#ax.title(title.format( year, month, day, hh, mm), fontsize=10)

	#ax.show()
