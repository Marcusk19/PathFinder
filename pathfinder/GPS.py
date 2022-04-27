"""
GPS module
----------
The GPS module handles the reading of data from our UBLOX chip via gpsd.
It contains two helper functions: one to get coordinates for the current location,
and one to calculate the distance between two coordinate points.
"""
from gps import *
import geopy.distance

class GPS_controller():
    def __init__(self):
        global gpsd 
        gpsd = gps(mode=WATCH_ENABLE)

    def get_coordinates(self):
        """Returns latitude and longitude of current location.

        Returns:
            (float, float): Tuple of floating point coordinates.
        """
        global gpsd
        gpsd.next()
        return (gpsd.fix.latitude, gpsd.fix.longitude)

    def calculate_distance(self, cords1, cords2):
        """Returns a distance in miles given two coordinate points.

        Args:
            cords1 (float, float): Tuple of point A.
            cords2 (float, float): Tuple of point B.

        Returns:
            float: Distance between point A and point B.
        """
        distance =  geopy.distance.geodesic(cords1, cords2).miles
        return float("{:.2f}".format(distance))
