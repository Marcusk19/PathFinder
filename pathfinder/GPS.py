from gps import *
import geopy.distance

class GPS(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self) # initialization of thread
        gpsd = gps(mode=WATCH_ENABLE)

    def get_coordinates(self):
        return (self.gpsd.fix.latitude, self.gpsd.fix.longitude)

    def calculate_distance(self, cords1, cords2):
        return geopy.distance.geodesic(cords1, cords2).miles
