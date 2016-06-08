import arcpy
from arcpy import env
import os

arcpy.env.overwriteOutput = True

##################################################
###PLEASE NOTE YOU MAY HAVE TO MODIFY#############
###YOUR DATABASE CONNECTIONS AND DRIVE MAPPING####
###FOR THIS SCRIPT TO WORK ON YOUR MACHINE########
##################################################

# Set local variables
sewer_in_data =  "Database Connections\CITY_RALEIGH_TESTDB.sde\RPUD.SewerCollectionNetwork"
print "IN data source is " + sewer_in_data
sewer_out_data = "U:/CCTV/CCTV.gdb/SewerCollectionNetwork"
print "Data will be copied to " + sewer_out_data
street = "Database Connections\WAKE_PRODDB.sde\WAKE.STREET"
parcel = "Database Connections\WAKE_PRODDB.sde\WAKE.PROPERTY_A_RECORDED"
etj = "Database Connections\WAKE_PRODDB.sde\WAKE.JURISDICTION"
basin = "Database Connections\CITY_RALEIGH_TESTDB.sde\RPUD.PU_Boundaries\RPUD.SewerBasins"

out_basemap = "U:/CCTV/BASEMAP.gdb"

#delete data first
delete_data = "U:/CCTV/CCTV.gdb"
delete_basemap_data = "U:/CCTV/BASEMAP.gdb"

#Clean up existing data
# Execute Delete
arcpy.Delete_management(delete_data)
print "Sewer geodatabase deleted"
arcpy.Delete_management(delete_basemap_data)
print "Basemap geodatabase deleted"

#create new geodatabases
arcpy.CreateFileGDB_management("U:/CCTV", "CCTV.gdb")
arcpy.CreateFileGDB_management("U:/CCTV", "BASEMAP.gdb")

# Execute Copy
arcpy.Copy_management(sewer_in_data, sewer_out_data)
print "Data copied to " + sewer_out_data

arcpy.FeatureClassToGeodatabase_conversion(street, out_basemap)
print "Street data copied to " + out_basemap

arcpy.FeatureClassToGeodatabase_conversion(parcel, out_basemap)
print "Parcel data copied to " + out_basemap

arcpy.FeatureClassToGeodatabase_conversion(etj, out_basemap)
print "ETJ data copied to " + out_basemap

arcpy.FeatureClassToGeodatabase_conversion(basin, out_basemap)
print "Sewer Basin data copied to " + out_basemap
