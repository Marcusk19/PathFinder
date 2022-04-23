from gps import *
import geopy.distance

class GPS_controller():
    def __init__(self):
        global gpsd 
        gpsd = gps(mode=WATCH_ENABLE)

    def get_coordinates(self):
        global gpsd
        gpsd.next()
        return (gpsd.fix.latitude, gpsd.fix.longitude)

    def calculate_distance(self, cords1, cords2):
        distance =  geopy.distance.geodesic(cords1, cords2).miles
        return float("{:.2f}".format(distance))
