# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:20:41 2019

@author: JacobNordberg
"""

import arcpy
from arcpy import env
#import os

env.workspace           =   r'C:\USS\United States Solar Corporation\Site Selection - Documents\Data\State\ME\ME.gdb\Physical'
env.overwriteOutput     =   True
out_flood               =   "FloodData"
featureclasses          =   arcpy.ListFeatureClasses()
floodData               =   []
# Copy shapefiles to a file geodatabase
for fc in featureclasses:
    if fc.endswith("_Flood"):
        arcpy.Select_analysis(fc, '{}_{}'.format(out_flood, fc), "FLD_ZONE IN ('A', 'AO', 'AE')")
    floodData.append('{}_{}'.format(out_flood, fc))
floodData.remove("FloodData_ME_Wetlands")
floodData.remove("FloodData_ME_Countours_10")
arcpy.Merge_management(floodData, "stateWideFloodHazard")
for i in floodData:
    arcpy.Delete_management(i)
