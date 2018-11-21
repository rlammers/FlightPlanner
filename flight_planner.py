"""
Run the flight planner as a console application.
"""
import getopt
import sys
from flight import Flight
from airport_service import AirportService
from flight_schedule import FlightSchedule

USAGE_MESSAGE = 'airports.py -i <inputfile> -o <originicao> -u <unitsofdistance>'


def populate_dest_airports(origin, dest_airports, all_airports):
    for airport in all_airports:
        if origin.icao != airport.icao:
            dest_airports.append(airport)


def traverse_airports(dest_airports, previous_airport, units):
    flights = []
    dest_airports.remove(previous_airport)
    while len(dest_airports) >= 1:
        close_airport = previous_airport.closest_airport(dest_airports, units)
        close_dist = previous_airport.distance_to(close_airport, units)
        flight = Flight(previous_airport, close_airport, close_dist, units)
        flights.append(flight)
        previous_airport = close_airport
        dest_airports.remove(close_airport)
    return flights


def return_to_origin(origin, previous_airport, units):
    dest_airports = [origin]
    close_airport = previous_airport.closest_airport(dest_airports, units)
    close_dist = previous_airport.distance_to(close_airport, units)
    flight = Flight(previous_airport, close_airport, close_dist, units)

    return flight


def get_airport(icao, airports):
    for airport in airports:
        if icao == airport.icao:
            return airport
    return None


def total_distance(flights):
    total = 0
    for flight in flights:
        total = total + flight.distance
    return total


def create_flightplan(airports, origin, units):
    flights = traverse_airports(airports, origin, units)
    final_stop = flights[-1].destination
    return_flight = return_to_origin(origin, final_stop, units)
    flights.append(return_flight)
    return flights


def setup_origin(airports, origin_icao):
    if origin_icao == '':
        origin_icao = input("Please enter ICAO code for origin: ")
    origin = get_airport(origin_icao, airports)
    return origin


def main(argv):
    if not argv:
        print(USAGE_MESSAGE)
        sys.exit()

    origin_icao = ''
    units = ''

    try:
        opts = getopt.getopt(argv, "ho:u:", [])
    except getopt.GetoptError:
        print(USAGE_MESSAGE)
        sys.exit(2)
    for opt, arg in opts[0]:
        if opt == '-h':
            print(USAGE_MESSAGE)
            sys.exit()
        elif opt in ("-o", "--origin"):
            origin_icao = arg.strip()
        elif opt in ("-u", "--units"):
            units = arg

    if units == '':
        units = 'km'

    airport_service = AirportService()
    airports = airport_service.get_airports()

    flight_schedule = FlightSchedule(origin_icao, airports)
    flight_schedule.create_flightplan(units)
    flight_schedule.print_flights()

    # TODO: Draw flight path lines between the airports for each flight
    # features = flightSchedule.to_geojson()


if __name__ == "__main__":
    main(sys.argv[1:])
