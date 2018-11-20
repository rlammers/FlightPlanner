"""
A single flight
"""
from geojson import LineString

class Flight():
    """
    Flight object has an origin, destination and a calculated distance
    between them. As well as the units for the distance. It can be printed
    to a string or as GeoJSON.
    """
    origin = None
    destination = None
    distance = None
    units = ''

    def __init__(self, origin, destination, distance, units):
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.units = units

    def __str__(self):
        return "-" + self.origin.city + " to " + self.destination.city + \
               " = " + str(int(self.distance)) + " " + self.units

    def to_geojson(self):
        """
        Use GeoJSON library to create and return a line string representing the flight
        """
        origin_coordinates = (self.origin.longitude, self.origin.latitude)
        destination_coordinates = (self.destination.longitude, self.destination.latitude)
        line_string = LineString(coordinates=([origin_coordinates, destination_coordinates]))
        return line_string
