from Flight import Flight
from geojson import FeatureCollection, Feature, Point
import copy

class FlightSchedule:
    origin = None
    airports = []

    def __init__(self, origin_icao, airports):
        self.airports = airports
        self.setup_origin(airports, origin_icao)

    @staticmethod
    def get_airport(icao, airports):
        for airport in airports:
            if icao == airport.icao:
                return airport

    @classmethod
    def setup_origin(cls, airports, origin_icao):
        if origin_icao == '':
            raise ValueError("Origin cannot be empty")
        cls.origin = cls.get_airport(origin_icao, airports)

    @staticmethod
    def traverse_airports(self, units):
        flights = []
        dest_airports = copy.deepcopy(self.airports)

        previous_airport = self.origin
        dest_airports = self.remove_airport_from_list(self, previous_airport, dest_airports)

        while len(dest_airports) >= 1:
            close_airport = previous_airport.closest_airport(dest_airports, units)
            close_dist = previous_airport.distance_to(close_airport, units)
            flight = Flight(previous_airport, close_airport, close_dist, units)
            flights.append(flight)
            previous_airport = close_airport
            self.remove_airport_from_list(self, close_airport, dest_airports)
        
        return flights

    @staticmethod
    def remove_airport_from_list(self, airport_to_remove, airport_list):
        for airport in airport_list:
            if airport.icao == airport_to_remove.icao:
                airport_list.remove(airport)
                return airport_list


    @classmethod
    def return_to_origin(cls, previous_airport, units):
        dest_airports = [cls.origin]
        close_airport = previous_airport.closest_airport(dest_airports, units)
        close_dist = previous_airport.distance_to(close_airport, units)
        flight = Flight(previous_airport, close_airport, close_dist, units)

        return flight


    def create_flightplan(self, units):
        flights = self.traverse_airports(self, units)
        final_stop = flights[-1].destination
        return_flight = self.return_to_origin(final_stop, units)
        flights.append(return_flight)
        return flights

    def to_geojson(self):
        features = []
        for airport in self.airports:
            feature = airport.to_geojson()
            features.append(feature)
        feature_collection = FeatureCollection(features)
        return feature_collection