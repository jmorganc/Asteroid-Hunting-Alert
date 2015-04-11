import ephem


"""
Get an observer location
Find all asteroids in the next 48 hours visible from that location
    Will also need to consider weather and light pollution
"""
class Hunter(ephem.Observer):

    def __init__(self):
        ephem.__init__(self)

    def something(self):
        pass