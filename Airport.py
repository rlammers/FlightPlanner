from geojson import Point, Feature, FeatureCollection

class Airport(object):
    icao = ''
    latitude = 0
    longitude = 0
    city = ''

    def __init__(self, icao, latitude, longitude, city):
        self.icao = icao
        self.latitude = latitude
        self.longitude = longitude
        self.city = city


    def to_geojson(self):
        point =  Point([self.latitude, self.longitude])
        feature = Feature(id=None, geometry=point)
        feature_collection = FeatureCollection(features=[feature])
        return feature_collection
