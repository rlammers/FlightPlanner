from Flight import Flight

class FlightSchedule:
    origin = None
    airports = []

    def __init__(self, origin_icao, airports):
        self.airports = airports
        self.origin = self.setup_origin(airports, origin_icao)

    @staticmethod
    def get_airport(icao, airports):
        for airport in airports:
            if icao == airport.icao:
                return airport

    @classmethod
    def setup_origin(self, airports, origin_icao):
        if origin_icao == '':
            raise ValueError("Origin cannot be empty")
        origin = self.get_airport(origin_icao, airports)
        return origin

    @classmethod
    def traverse_airports(cls, units):
        flights = []
        dest_airports = cls.airports
        previous_airport = cls.origin
        #dest_airports.remove(previous_airport)
        while len(dest_airports) >= 1:
            close_airport = previous_airport.closest_airport(dest_airports, units)
            close_dist = previous_airport.distance_to(close_airport, units)
            flight = Flight(previous_airport, close_airport, close_dist, units)
            flights.append(flight)
            previous_airport = close_airport
            dest_airports.remove(close_airport)
        return flights


    @classmethod
    def return_to_origin(cls, previous_airport, units):
        dest_airports = [cls.origin]
        close_airport = previous_airport.closest_airport(dest_airports, units)
        close_dist = previous_airport.distance_to(close_airport, units)
        flight = Flight(previous_airport, close_airport, close_dist, units)

        return flight


    def create_flightplan(self, units):
        flights = self.traverse_airports(units)
        final_stop = flights[-1].destination
        return_flight = self.return_to_origin(final_stop, units)
        flights.append(return_flight)
        return flights