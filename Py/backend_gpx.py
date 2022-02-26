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
The Gps class contains all of the methods to handle the gpx data manipulation
all the way from parsing the gpx file to visualize the maptacked and total
distance of the track in e.g OpenStreetView
"""
#-------------- Classes --------------#
# Gps class
__GPS__ = []
class Gps:
    def __init__(self, file):
       self.file = file 

    def __repr__(self):
       return np.array(self) 

    def parse(self):
        # Open gpx file
        gpx_file = open(self.file, mode='rt', encoding ='utf-8')
        # Parse gpx file 
        self.gpx = gpxpy.parse(gpx_file)
        return self.gpx 

    def loc(self):
        gpx = self.parse()
        # Loop to collect lon, lat and ele
        loc = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points: 
                    loc.append([point.latitude,
                                point.longitude])
        return np.array(loc)
    
    def rdp(self):
        """
        Applying the Ramer-Douglas-Peucker algoritm. This is done by calling loc()
        and return the updated points, have to look how to do this in a profesional way
        """
        loc = self.loc()