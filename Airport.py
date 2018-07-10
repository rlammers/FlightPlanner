class Airport(object):
    icao = ''
    latitude = 0
    longitude = 0
    city = ''
    metar = ''

    def __init__(self, icao, latitude, longitude, city):
        self.icao = icao
        self.latitude = latitude
        self.longitude = longitude
        self.city = city

    def set_metar(self, metar):
        self.metar = metar

    def get_metar(self):
        return self.metar

    @staticmethod
    def validate_metar(metar):
        metars = metar.split(' ')
        if metars[0] == "METAR":
            return True
        else:
            return False

    def validate_icao(self, metar_icao):
        if metar_icao == self.icao:
            return True
        else:
            return False

    def to_geojson(self):
        return {"coordinates": [self.latitude, self.longitude]}
