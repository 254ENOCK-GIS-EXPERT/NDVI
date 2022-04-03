# NDVI
How to create ndvi using GEE GOOGLE COLAB.
#Import the google earth engine(ee) package into your working directory as below

import ee
# Install the geemap function
!pip install geemap
import geemap

#Create google earth engine account. Connect to the google earth engine, and connect to your google account

ee.Authenticate()
ee.Initialize()
# import boundary shapefile, for the study area for our case - :ee.FeatureCollection("users/ENOCKO/kiambu_boundary")

# obtaininng the region of interest using an input.
roi = ee.FeatureCollection("users/ENOCKO/kiambu_boundary")
Map = geemap.Map()

#use the NDVI formular -> NIR.subtract(RED).divide(NIR.add(RED))

sentinel = ee.ImageCollection("COPERNICUS/S2_SR")
data = sentinel.filterBounds(roi).filterDate('2020-03-28', '2020-05-01').mean()

RED = data.select('B4')
NIR = data.select('B8')

NDVI = NIR.subtract(RED).divide(NIR.add(RED))
NDVIc = NDVI.clip(roi);

Map.centerObject(roi, 9);
Map.addLayer(NDVIc)
Map
