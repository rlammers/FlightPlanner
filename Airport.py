class Airport(object):
    icao = ''
    latitude = 0
    longitude = 0

    def __init__(self, icao, latitude, longitude):
        self.icao = icao
        self.latitude = latitude
        self.longitude = longitude
