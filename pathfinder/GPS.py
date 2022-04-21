from gps import *
import geopy.distance

class GPS_controller():
    def __init__(self):
        self.gpsd = gps(mode=WATCH_ENABLE)

    def get_coordinates(self):
        self.gpsd.next()
        return (self.gpsd.fix.latitude, self.gpsd.fix.longitude)

    def calculate_distance(self, cords1, cords2):
        return geopy.distance.geodesic(cords1, cords2).miles
