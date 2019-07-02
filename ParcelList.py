# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 11:33:26 2019

@author: JacobNordberg
"""
import arcpy
from arcpy import env

env.workspace           =   r'C:\USS\United States Solar Corporation\Site Selection - Documents\Data\State\NV\Nevada20190411.gdb'
env.overwriteOutput     =   True

util                    =   "UtilityData/NV_Energy_Service_Territory"
county                  =   "Political/NV_County"
phi                     =   "_DeleteTemp"


def createParcelList(poly, utility):
    arcpy.Intersect_analysis([county, util], "out_counties"+phi)

    
createParcelList(county, util)