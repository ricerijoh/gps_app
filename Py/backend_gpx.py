"""
This Python script is designed to hold all of the back en functions for the Application
Start date: 21/2 - 2022
Author: Richard Johansson
"""
# Imports
import gpxpy
import numpy as np
import matplotlib.pyplot as plt
from geopy import distance 
"""
Is a Class the way to go? a lot of functions to do various
things with multiple imported gpx files will be done and 
to work with objects will most likey be the way to go.

Will also build a Django integration with the front end 
and it could be a class of its own.
"""
#-------------- Classes --------------#
class Gps:
    def __init__(self, file):
       self.file = file 

    def __repr__(self):
       return np.array(self) 
         
    def get_lat_lon_ele(self):
        # Open gpx file
        gpx_file = open(self.file, mode='rt', encoding ='utf-8')
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
        return np.array(lle)

        
    def plotPoints(self):
        lle = self.get_lat_lon_ele()
        plt.plot(lle[:,0],
                 lle[:,1], 'r.')


file = Gps('data/Walk1.gpx')
dis , ele = file.gps_distance_elevation()