"""
This Python script is designed to hold all of the back en functions for the Application
Start date: 21/2 - 2022
Author: Richard Johansson
"""
# Imports
import gpxpy
import numpy as np
from leuvenmapmatching.util.gpx import gpx_to_path
import matplotlib.pyplot as plt
import pandas as pd
from geopy import distance 
from rdp import rdp
"""
The Gps class contains all of the methods to handle the gpx data manipulation
all the way from parsing the gpx file to visualize the maptacked and total
distance of the track in e.g OpenStreetView
"""
#-------------- Classes --------------#
# Gps class
class Gps:
    def __init__(self, files):
       self.files = files 
       self.coords = pd.DataFrame()
       self.rdp = pd.DataFrame()

       # RDP settings:
       self.epsilon = 5e-6
       self.algo = "iter"

    def __repr__(self):
       return np.array(self) 

    def get_lonlat(self):
        tracks = [gpx_to_path(idx) for idx in self.files]
        lat = list()
        lon = list()

        for i in range(len(tracks)):
            lat.extend([tracks[i][j][0] for j in range(len(tracks[i]))])
            lon.extend([tracks[i][j][1] for j in range(len(tracks[i]))])

        self.coords["lat"] = lat
        self.coords["lon"] = lon 

    def rdp_gps(self):
        """
        Applying the Ramer-Douglas-Peucker algoritm. This is done by calling loc()
        and return the updated points, have to look how to do this in a profesional way
        """
        temp = np.array(rdp(self.coords, epsilon = self.epsilon, algo = self.algo))
        self.rdp = pd.DataFrame(data = {'lat': temp[:,0], 'lon': temp[:,1]})

files = ["data/gps1.gpx", "data/gps2.gpx"]
data = Gps(files)
data.get_lonlat()
data.rdp_gps()


plt.figure()
plt.plot(data.coords.lat, data.coords.lon, "r.", label = "Concatinated gps points from two files")
plt.plot(data.rdp.lat, data.rdp.lon, "b.", label = "Ponts reduced with Ramer-Douglas-Peucker algorithm")
plt.legend(loc = "best", fontsize = 8)
plt.show()
