from .geometry import get_proj_params
from .modismeta_read import parseMeta
from pyhdf.SD import SD, SDC
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from pathlib import Path
import cartopy
from pyproj import transform as proj_transform
from pyproj import Proj
import pandas as pd
from pathlib import Path
from .read_aeronet import read_aeronet
from pyresample import SwathDefinition


def get_area_def(hdf_file):
    generic_m3 = str(hdf_file)
    metadata = parseMeta(generic_m3)

    # Read the lats and lons from the MYD03 file
    print(f'reading {generic_m3}')
    m3_file = SD(str(generic_m3), SDC.READ)
    lats = m3_file.select('Latitude').get()
    lons = m3_file.select('Longitude').get()
    m3_file.end()



    proj_params = get_proj_params(generic_m3)
    swath_def = SwathDefinition(lons, lats)
    area_def=swath_def.compute_optimal_bb_area(proj_dict=proj_params)

    return(area_def, lons, lats, metadata, swath_def)


def plot_geom(hdf_file, stn_lon, stn_lat):
    """
    given an hdf file creats a plot with diagonal corner line with upper
    and lower edge of swath with a projection centre point. plots station
    with given coordinates in lon lat

    Parameters
    ----------

    hdf_file:  Path or str with path to hdf file

    Returns
    -------

    proj_params: axis with large plot

    """

    area_def, lons, lats, metadata, swath_def = get_area_def(hdf_file)


    #Transfom lats and longs into gridded goordinates on projection

    p_lonlat=Proj(proj='latlong',datum='WGS84')
    stn_x, stn_y = proj_transform(p_lonlat, Proj(area_def.proj_dict), stn_lon, stn_lat)
    swath_x, swath_y = proj_transform(p_lonlat, Proj(area_def.proj_dict), lons, lats)
    min_x, min_y =  proj_transform(p_lonlat, Proj(area_def.proj_dict), metadata['min_lon'],  metadata['min_lat'])
    max_x, max_y =  proj_transform(p_lonlat, Proj(area_def.proj_dict), metadata['max_lon'], metadata['max_lat'])
    xis = [min_x, max_x]
    yis = [min_y, max_y]
    crs = area_def.to_cartopy_crs()




#def make_plot(swath_x, swath_y, stn_x, stn_y, area_def, xis, yis):

    crs = area_def.to_cartopy_crs()


    fig, ax = plt.subplots(1, 1, figsize=(15,15),
                              subplot_kw={'projection': crs})
    ax.gridlines(linewidth=2)
    ax.add_feature(cartopy.feature.GSHHSFeature(levels=[1,2,3])); #scale='coarse'
    ax.set_extent(crs.bounds, crs)

    ax.scatter(0,0, marker= 'o', color='k', label = 'Projection centre')
    ax.scatter(stn_x, stn_y, marker= 'x', color='r', label = 'ground station')
    ax.scatter(swath_x[0:10], swath_y[0:10], marker= 'o', color='r', label = 'swath bound lower')
    ax.scatter(swath_x[-10:-1], swath_y[-10:-1], marker= 'o', color='r', label = 'swath bound upper')
    ax.plot(xis, yis, label='Corners Connect')

    #ax.set(title= str(generic_m3))
    ax.legend();







if __name__=='__main__':
    sys.exit(main())
