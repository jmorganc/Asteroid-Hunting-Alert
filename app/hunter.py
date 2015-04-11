import ephem


"""
Get an observer location
Find all asteroids in the next 48 hours visible from that location
    Will also need to consider weather and light pollution
"""
class Hunter(object):

    observer = None

    def __init__(self, datetime, lon, lat):
        self.observer = ephem.Observer()
        self.observer.date = datetime
        self.observer.lon = lon
        self.observer.lat = lat
