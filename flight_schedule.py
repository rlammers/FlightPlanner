import copy

from geojson import FeatureCollection

from flight import Flight


class FlightSchedule:
    UNITS = "km"

    def __init__(self, origin_icao, airports, units=None):
        self.airports = airports
        self._flights = []
        self._origin = None
        self.units = units or self.UNITS
        self.setup_origin(origin_icao)

    @staticmethod
    def get_airport(icao, airports):
        for airport in airports:
            if icao == airport.icao:
                return airport

    def setup_origin(self, origin_icao):
        if origin_icao == '':
            raise ValueError("Origin cannot be empty")
        self._origin = self.get_airport(origin_icao, self.airports)
        if self._origin is None:
            raise ValueError(f"Origin airport not found: {origin_icao}")

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

    def return_to_origin(self, previous_airport, units):
        dest_airports = [self._origin]
        close_airport = previous_airport.closest_airport(dest_airports, units)
        close_dist = previous_airport.distance_to(close_airport, units)
        flight = Flight(previous_airport, close_airport, close_dist, units)

        return flight

    def create_flightplan(self, units=None):
        if units is None:
            units = self.units
        else:
            self.units = units

        self._flights = self.traverse_airports(units)
        if not self._flights:
            return

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
        print(str(int(self.total_distance(self._flights))) + self.units)

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
