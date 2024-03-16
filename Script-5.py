#!/usr/bin/env python
# coding: utf-8

# #### Suitability Raster Analysis
# ##### Question 1
# Please create a Model in either ArcGIS Pro for the Bobcat habitat example we discussed in class and export your model as both a python script and a image (lab5.py and lab5.jpg - 15 points) 

# In[9]:


import arcpy
from arcpy.sa import *

#workplace location
arcpy.env.workspace = "C:\\Users\\akunna1\\Desktop\\GEOG 592\\Lab_5\\Data.gdb\\"
arcpy.env.overwriteOutput = True

# Checking out necessary licenses
arcpy.CheckOutExtension("3D")
arcpy.CheckOutExtension("spatial")
arcpy.CheckOutExtension("ImageAnalyst")

# Setting up Geoprocessing environments
arcpy.env.snapRaster = "C:\\Users\\akunna1\\Desktop\\GEOG 592\\Lab_5\\Data.gdb\\Elevation"
arcpy.env.extent = "439952.113762345 200181.284694512 513122.113762345 253671.284694512"
arcpy.env.cellSize = "30"
arcpy.env.mask = "C:\\Users\\akunna1\\Desktop\\GEOG 592\\Lab_5\\Data.gdb\\Elevation"

Streams = "C:\\Users\\akunna1\\Desktop\\GEOG 592\\Lab_5\\Data.gdb\\Streams"
Elevation = arcpy.Raster("C:\\Users\\akunna1\\Desktop\\GEOG 592\\Lab_5\\Data.gdb\\Elevation")
LandUse = arcpy.Raster("C:\\Users\\akunna1\\Desktop\\GEOG 592\\Lab_5\\Data.gdb\\LandUse")

# Process: Distance Accumulation (Distance Accumulation) (sa)
Distanc_Stre1 = "Distanc_Stre1"
Distance_Accumulation = Distanc_Stre1
blkRaster = "blkRaster"
osdr = "osdr"
oslr = "oslr"
Distanc_Stre1 = arcpy.sa.DistanceAccumulation(in_source_data=Streams, vertical_factor="BINARY 1 -30 30", horizontal_factor="BINARY 1 45", out_back_direction_raster=blkRaster, out_source_direction_raster=osdr, out_source_location_raster=oslr, distance_method="PLANAR")
Distanc_Stre1.save(Distance_Accumulation)

blkRaster = arcpy.Raster(blkRaster)
osdr = arcpy.Raster(osdr)
oslr = arcpy.Raster(oslr)

# Process: Slope (Slope) (sa)
Slope_Elevat1 = "Slope_Elevat1"
Slope = Slope_Elevat1
Slope_Elevat1 = arcpy.sa.Slope(in_raster=Elevation, output_measurement="DEGREE", z_factor=0.30480060960121924, method="PLANAR", z_unit="Foot_US")
Slope_Elevat1.save(Slope)

# Process: Reclassify (Reclassify) (sa)
Reclass_Slop1 = "Reclass_Slop1"
Reclassify = Reclass_Slop1
Reclass_Slop1 = arcpy.sa.Reclassify(in_raster=Slope_Elevat1, reclass_field="VALUE", remap="0 3 1;3 10 3;10 25 6;25 90 10", missing_values="DATA")
Reclass_Slop1.save(Reclassify)

# Process: Reclassify (2) (Reclassify) (sa)
Reclass_Land1 = "Reclass_Land1"
Reclassify_2_ = Reclass_Land1
Reclass_Land1 = arcpy.sa.Reclassify(in_raster=LandUse, reclass_field="VALUE", remap="1 1;2 1;3 1;4 2;5 8;6 10;7 10;8 10;9 6;10 2;11 10;12 1", missing_values="DATA")
Reclass_Land1.save(Reclassify_2_)

# Process: Rescale by Function (Rescale by Function) (sa)
Rescale_Dist1 = "Rescale_Dist1"
Rescale_by_Function = Rescale_Dist1
Rescale_Dist1 = arcpy.sa.RescaleByFunction(in_raster=Distanc_Stre1, transformation_function=[["MSSMALL", "", "", "", "", 1, 1, ""]], from_scale=1, to_scale=10)
Rescale_Dist1.save(Rescale_by_Function)

# Process: Raster Calculator (Raster Calculator) (sa)
reclas_raste = "reclas_raste"
Raster_Calculator = reclas_raste
reclas_raste =  Reclass_Slop1 *0.3 + Reclass_Land1 *0.3 + Rescale_Dist1 *0.4
reclas_raste.save(Raster_Calculator)


# ##### Question 2
# Modify the script (lab5.py) so it will allow a user to configure weights of slope, landuse, and distance to streams. (10 points)

# In[10]:


import arcpy
from arcpy.sa import *

#workplace location
arcpy.env.workspace = "C:\\Users\\akunna1\\Desktop\\GEOG 592\\Lab_5\\Data.gdb\\"
arcpy.env.overwriteOutput = True

# Checking out necessary licenses
arcpy.CheckOutExtension("3D")
arcpy.CheckOutExtension("spatial")
arcpy.CheckOutExtension("ImageAnalyst")

# Setting up Geoprocessing environments
arcpy.env.snapRaster = "C:\\Users\\akunna1\\Desktop\\GEOG 592\\Lab_5\\Data.gdb\\Elevation"
arcpy.env.extent = "439952.113762345 200181.284694512 513122.113762345 253671.284694512"
arcpy.env.cellSize = "30"
arcpy.env.mask = "C:\\Users\\akunna1\\Desktop\\GEOG 592\\Lab_5\\Data.gdb\\Elevation"

Streams = "C:\\Users\\akunna1\\Desktop\\GEOG 592\\Lab_5\\Data.gdb\\Streams"
Elevation = arcpy.Raster("C:\\Users\\akunna1\\Desktop\\GEOG 592\\Lab_5\\Data.gdb\\Elevation")
LandUse = arcpy.Raster("C:\\Users\\akunna1\\Desktop\\GEOG 592\\Lab_5\\Data.gdb\\LandUse")

# Process: Distance Accumulation (Distance Accumulation) (sa)
Distanc_Stre1 = "Distanc_Stre1"
Distance_Accumulation = Distanc_Stre1
blkRaster = "blkRaster"
osdr = "osdr"
oslr = "oslr"
Distanc_Stre1 = arcpy.sa.DistanceAccumulation(in_source_data=Streams, vertical_factor="BINARY 1 -30 30", horizontal_factor="BINARY 1 45", out_back_direction_raster=blkRaster, out_source_direction_raster=osdr, out_source_location_raster=oslr, distance_method="PLANAR")
Distanc_Stre1.save(Distance_Accumulation)

blkRaster = arcpy.Raster(blkRaster)
osdr = arcpy.Raster(osdr)
oslr = arcpy.Raster(oslr)

# Process: Slope (Slope) (sa)
Slope_Elevat1 = "Slope_Elevat1"
Slope = Slope_Elevat1
Slope_Elevat1 = arcpy.sa.Slope(in_raster=Elevation, output_measurement="DEGREE", z_factor=0.30480060960121924, method="PLANAR", z_unit="Foot_US")
Slope_Elevat1.save(Slope)

# Process: Reclassify (Reclassify) (sa)
Reclass_Slop1 = "Reclass_Slop1"
Reclassify = Reclass_Slop1
Reclass_Slop1 = arcpy.sa.Reclassify(in_raster=Slope_Elevat1, reclass_field="VALUE", remap="0 3 1;3 10 3;10 25 6;25 90 10", missing_values="DATA")
Reclass_Slop1.save(Reclassify)

# Process: Reclassify (2) (Reclassify) (sa)
Reclass_Land1 = "Reclass_Land1"
Reclassify_2_ = Reclass_Land1
Reclass_Land1 = arcpy.sa.Reclassify(in_raster=LandUse, reclass_field="VALUE", remap="1 1;2 1;3 1;4 2;5 8;6 10;7 10;8 10;9 6;10 2;11 10;12 1", missing_values="DATA")
Reclass_Land1.save(Reclassify_2_)

# Process: Rescale by Function (Rescale by Function) (sa)
Rescale_Dist1 = "Rescale_Dist1"
Rescale_by_Function = Rescale_Dist1
Rescale_Dist1 = arcpy.sa.RescaleByFunction(in_raster=Distanc_Stre1, transformation_function=[["MSSMALL", "", "", "", "", 1, 1, ""]], from_scale=1, to_scale=10)
Rescale_Dist1.save(Rescale_by_Function)

# Process: Raster Calculator (Raster Calculator) (sa)
while(True):
    try:
        reclas_raste = "reclas_raste"
        Raster_Calculator = reclas_raste
        user_input = input('Input the weight for the slope, landuse, and Distance to stream(e.g. 1.2 0.5 0.1):')
        weight = user_input.split()
        reclas_raste =  Reclass_Slop1 **float(weight[0]) + Reclass_Land1 **float(weight[1]) + Rescale_Dist1 **float(weight[2])
        reclas_raste.save(Raster_Calculator)
        print('Completed!')
        break
    except ValueError:
        print('Invalid Input! Try Again.')


# In[ ]:




