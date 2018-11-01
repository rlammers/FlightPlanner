from geojson import Point, Feature, FeatureCollection
from geopy import distance
from functools import lru_cache

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

    @lru_cache(maxsize=None)
    def distance_to(self, destination, units):
        departure_coords = (self.latitude, self.longitude)
        arrival_coords = (destination.latitude, destination.longitude)
        
        if units.lower() == 'nm':
            return distance.great_circle(departure_coords, arrival_coords).nm
        elif units.lower() == 'km':
            return distance.great_circle(departure_coords, arrival_coords).km
        else:
            raise ValueError('Invalid unit specified when calculating distance between airports.')
