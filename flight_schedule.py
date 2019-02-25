import copy

from geojson import FeatureCollection

from flight import Flight


class FlightSchedule:
    _origin = None
    _airports = []
    _flights = []
    # TODO: Make units passed in as a param rather than constant
    UNITS = "km"

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
        cls._origin = cls.get_airport(origin_icao, airports)

    @staticmethod
    def traverse_airports(self, units):
        flights = []
        dest_airports = copy.deepcopy(self.airports)

        previous_airport = self._origin
        dest_airports = self.remove_airport_from_list(previous_airport, dest_airports)

        while len(dest_airports) >= 1:
            close_airport = previous_airport.closest_airport(dest_airports, units)
            close_dist = previous_airport.distance_to(close_airport, units)
            flight = Flight(previous_airport, close_airport, close_dist, units)
            flights.append(flight)
            previous_airport = close_airport
            self.remove_airport_from_list(close_airport, dest_airports)
        
        return flights

    @staticmethod
    def remove_airport_from_list(airport_to_remove, airport_list):
        for airport in airport_list:
            if airport.icao == airport_to_remove.icao:
                airport_list.remove(airport)
                return airport_list

    @classmethod
    def return_to_origin(cls, previous_airport, units):
        dest_airports = [cls._origin]
        close_airport = previous_airport.closest_airport(dest_airports, units)
        close_dist = previous_airport.distance_to(close_airport, units)
        flight = Flight(previous_airport, close_airport, close_dist, units)

        return flight

    def create_flightplan(self, units):
        self._flights = self.traverse_airports(self, units)
        final_stop = self._flights[-1].destination
        return_flight = self.return_to_origin(final_stop, units)
        self._flights.append(return_flight)

    def airports_to_geojson(self):
        features = []
        for airport in self.airports:
            feature = airport.to_geojson()
            features.append(feature)
        feature_collection = FeatureCollection(features)
        return feature_collection

    def get_flights(self):
        return self._flights

    def flights_to_geojson(self):
        features = []
        for flight in self._flights:
            feature = flight.to_geojson()
            features.append(feature)
        feature_collection = FeatureCollection(features)
        return feature_collection

    @staticmethod
    def total_distance(flights):
        total = 0
        for flight in flights:
            total = total + flight.distance
        return total

    def print_flights(self):
        for flight in self._flights:
            print(flight)
        print(str(int(self.total_distance(self._flights))) + self.UNITS)

    def to_geojson(self):
        features = []

        for airport in self.airports:
            feature = airport.to_geojson()
            features.append(feature)

        for flight in self._flights:
            feature = flight.to_geojson()
            features.append(feature)
            
        feature_collection = FeatureCollection(features)
        return feature_collection
