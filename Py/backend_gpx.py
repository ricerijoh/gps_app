"""
This Python script is designed to hold all of the back en functions for the Application
Start date: 21/2 - 2022
Author: Richard Johansson
"""
# Imports
import gpxpy

#-------------- Functions --------------#
def get_lat_lon_ele(path):
    # Open gpx file
    gpx_file = open(path, mode='rt', encoding ='utf-8')
    # Parse gpx file 
    gpx = gpxpy.parse(gpx_file)
    # Loop to collect lon, lat and ele
    lle = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                lle.append([point.latitude,
                            point.longitude,
                            point.elevation])
    return lle
