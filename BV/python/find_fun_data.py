# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.0.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
from pathlib import Path
from read_aeronet import read_aeronet
#from a301.geometry import get_proj_params, parseMeta
from geometry import get_proj_params
from modismeta_read import parseMeta
from pyhdf.SD import SD, SDC
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from pathlib import Path
from pyproj import transform as proj_transform
from pyproj import Proj
# %matplotlib inline

# %%
my_files = list(Path().glob('*lev20'))
print(my_files)
df = read_aeronet(my_files[0])

# %% {"scrolled": false}
ax = df.loc['2015-01-01':'2017-01-01','AOD_1020nm':'AOD_340nm'].plot(figsize=(20,10)) 
ax.axhline(1);

# %%
# home = Path.home()/'/Documents/knowledge/Year_5/Term_2/A448/HDF_file_TableMTN'
# hdf_files = list(home.glob('*hdf'))
# hdf_files

# print(generic_m3)
#get_proj_params(generic_m3)

generic_m3 = list(Path().glob('*hdf'))[0]
metadata = parseMeta(generic_m3)

# Read the lats and lons from the MYD03 file
print(f'reading {generic_m3}')
m3_file = SD(str(generic_m3), SDC.READ)
lats = m3_file.select('Latitude').get()
lons = m3_file.select('Longitude').get()
m3_file.end()

dir(metadata)


# %% {"scrolled": true}
from pyresample import load_area, save_quicklook, SwathDefinition
proj_params = get_proj_params(generic_m3)
swath_def = SwathDefinition(lons, lats)
area_def=swath_def.compute_optimal_bb_area(proj_dict=proj_params)
area_def

# %%
print(swath_def.shape)
print(area_def.shape)

# %% {"scrolled": false}
#p_utm = Proj(crs)
p_lonlat=Proj(proj='latlong',datum='WGS84')
stn_lon = -105.237
stn_lat = 40.125
stn_x, stn_y = proj_transform(p_lonlat, Proj(area_def.proj_dict), stn_lon, stn_lat) 
min_x, min_y =  proj_transform(p_lonlat, Proj(area_def.proj_dict), metadata['min_lon'],  metadata['min_lat'])
max_x, max_y =  proj_transform(p_lonlat, Proj(area_def.proj_dict), metadata['max_lon'], metadata['max_lat'])

# %%
crs = area_def.to_cartopy_crs()
fig, ax = plt.subplots(1, 1, figsize=(10,10),
                          subplot_kw={'projection': crs})
ax.gridlines(linewidth=2)
ax.add_feature(cartopy.feature.GSHHSFeature(levels=[1,2,3])); #scale='coarse'

ax.set_extent(crs.bounds,crs)
ax.scatter(0,0, marker= 'o', color='k', label = 'Projection centre')
ax.scatter(stn_x, stn_y, marker= 'x', color='r', label = 'station location')
ax.scatter(max_x, max_y,  marker= 'x', color='r',)
ax.scatter(swath_x[0:10], swath_y[0:10], marker= 'o', color='b', label = 'swath bound')
ax.scatter(swath_x[-10:-1], swath_y[-10:-1], marker= 'o', color='b', label = 'swath bound')
ax.legend();



# %%

# %%
