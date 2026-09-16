"""CONUS area-weighted mean of IPCC AR6 SPM.5 panel b2 (ΔT at 2 °C GWL).

Dependency: netcdf4
netcdf4 seems to come with its own netcdf library. However, on a Mac it will be more general to build from source with "brew install netcdf".
You'll get useful utilities like ncdump.

This file was drafted with Claude Opus 5:
https://assistant.kagi.com/share/c99f3dce-e716-4ab3-b684-3b62b71e62d9.
Note: it took several iterations; should have enforced doing a simple weighted average by cos(lat) to start
and avoiding it trying to do reprojections.
I added the diagnostics at the end: unweighted distribution, total land area, deg F, and pcolor plot.

The data being plotted are downloaded from CEDA, corresponding to IPCC AR5 WGI Summary for Policymakers, Fig 5.
https://data.ceda.ac.uk/badc/ar6_wg1/data/spm/spm_05/v20221116/v20221116
The data should look like this figure:
https://www.climate.us/news-features/understanding-climate/climate-change-global-temperature.

"""
import numpy as np
import geopandas as gpd
import shapely
from netCDF4 import Dataset
import pathlib
import pandas as pd
import matplotlib.pyplot as plt

NC = pathlib.Path().cwd() / 'inputdata' / "Panel_b2_Simulated_temperature_change_at_2C.nc"
# Census cartographic boundary file, 1:20M states (small, public, no auth)
STATES = "https://www2.census.gov/geo/tiger/GENZ2023/shp/cb_2023_us_state_20m.zip"
NON_CONUS = {"02", "15", "60", "66", "69", "72", "78"}  # AK, HI, AS, GU, MP, PR, VI
EARTH_RADIUS_KM = 6371
C_TO_F = 1.8 # deg F per deg C

outputdir = pathlib.Path().cwd() / 'outputdata'
outputdir.mkdir(exist_ok=True)


# --- 1. load -----------------------------------------------------------------
with Dataset(NC) as ds:
    lat = np.asarray(ds["lat"][:], dtype=float)
    lon = np.asarray(ds["lon"][:], dtype=float)
    # this file has dims (panel, lat, lon) plus a panel_char variable
    vname = next(v for v, var in ds.variables.items()
                 if {"lat", "lon"} <= set(var.dimensions))
    arr = ds[vname][:]
    print(f"{vname}: dims={ds[vname].dimensions} shape={arr.shape} "
          f"units={getattr(ds[vname], 'units', '?')}")

arr = np.squeeze(arr)              # drop a length-1 panel dim
assert arr.ndim == 2, f"pick a panel slice explicitly, shape={arr.shape}"
data = np.ma.masked_invalid(np.ma.masked_array(arr))

# --- 2. CONUS mask -----------------------------------------------------------
lon180 = ((lon + 180.0) % 360.0) - 180.0   # 0–360 -> -180–180 if needed
LON, LAT = np.meshgrid(lon180, lat) # expand lat and lon to 2D to match data
# lon, lat --> x, y

states = gpd.read_file(STATES)
conus = states.loc[~states["STATEFP"].isin(NON_CONUS)].to_crs("EPSG:4326")
conus_ll = conus.union_all()               # geopandas <1.0: conus.unary_union

# shapely 2.x vectorized point-in-polygon: no GeoSeries, no CRS bookkeeping
in_conus = shapely.contains_xy(conus_ll, LON, LAT)

# --- 3. cos(lat)-weighted mean ----------------------------------------------
w = np.cos(np.deg2rad(LAT) * in_conus * ~np.ma.getmaskarray(data))
w = np.where(in_conus & ~np.ma.getmaskarray(data), np.cos(np.deg2rad(LAT)), 0.0)

mean = float(np.sum(w * data.filled(0.0)) / np.sum(w))
print(f"cells in CONUS: {in_conus.sum()}")
print(f"CONUS area-weighted mean ΔT = {mean:.3f}")

print("Overall unweighted distribution using 'describe()':")

valid = ~np.ma.getmaskarray(data) * in_conus * data.filled(0)
valid = pd.DataFrame(valid).stack()
valid = valid[valid > 0]

print(pd.DataFrame(valid.describe())) # Have to stack the columns cause it's a rectangular grid.

# Check total inferred land area given each point is a 1 degree grid, with w weighted by cos(lat) above.
landarea = w.sum() * (2 * np.pi * EARTH_RADIUS_KM / 360)**2
# Each cell is a box of 2 pi R/180 * cos(lat). 
print(f"Inferred land area is {landarea / 1e6} million km^2.")

# Finally show deg F version
print(f"CONUS area-weighted mean ΔT in F = {mean * C_TO_F:.3f}")

# Drop a simple rectangular (non-projected) pcolor plot for diagnostic
masked = np.where(in_conus & ~np.ma.getmaskarray(data), data * C_TO_F, np.nan) # Remask values to nan
plt.pcolormesh(masked, cmap='jet', vmin=0)
plt.colorbar()
plt.title('Mean deg F Warming with 2C Global Warming')
plt.savefig(outputdir / 'conus_temp_2c_warming_cmip5.jpg')