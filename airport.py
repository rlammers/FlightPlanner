"""
Module to handle airport data including initialization, conversion to GeoJSON,
distance calculation, and finding the closest airport.
"""
from functools import lru_cache

from geojson import Point, Feature
from geopy import distance


class Airport(object):
    """
    Represents an airport with attributes such as ICAO code, latitude,
    longitude, and city. Provides methods for converting to GeoJSON format,
    calculating distances to other airports, and finding the closest airport.
    """
    icao = ''
    latitude = 0
    longitude = 0
    city = ''

    def __init__(self, icao, latitude, longitude, city):
        """
        Initialize an Airport object.

        :param icao: The ICAO code of the airport.
        :param latitude: The latitude of the airport.
        :param longitude: The longitude of the airport.
        :param city: The city where the airport is located.
        """
        self.icao = icao
        self.latitude = latitude
        self.longitude = longitude
        self.city = city

    def to_geojson(self):
        """
        Convert the airport data to GeoJSON format.

        :return: A GeoJSON Feature object representing the airport.
        """
        point = Point([self.longitude, self.latitude])
        feature = Feature(id=None, geometry=point, properties={"city": self.city})
        return feature

    @lru_cache(maxsize=1024)
    def distance_to(self, destination, units):
        """
        Calculate the great-circle distance to another airport.

        :param destination: The destination Airport object.
        :param units: The unit of measurement for the distance ('nm' or 'km').
        :return: The distance in the specified units.
        :raises ValueError: If an invalid unit is provided.
        """
        departure_coords = (self.latitude, self.longitude)
        arrival_coords = (destination.latitude, destination.longitude)

        if units.lower() == 'nm':
            return distance.great_circle(departure_coords, arrival_coords).nm
        elif units.lower() == 'km':
            return distance.great_circle(departure_coords, arrival_coords).km
        else:
            raise ValueError('Invalid unit specified when calculating distance between airports.')

    def closest_airport(self, airports, units):
        """
        Find the closest airport from a list of airports.

        :param airports: A list of Airport objects.
        :param units: The unit of measurement for the distance ('nm' or 'km').
        :return: The closest Airport object.
        """
        seen_dist = False
        closest_airport = None
        min_dist = 0

        for airport in airports:
            if not self.icao == airport.icao:
                current_dist = self.distance_to(airport, units)

                if current_dist < min_dist or not seen_dist:
                    closest_airport = airport
                    min_dist = current_dist
                seen_dist = True

        return closest_airport
