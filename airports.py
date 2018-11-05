import getopt
import sys
from Airport import Airport
from Flight import Flight
from airport_service import AirportService
from flight_schedule import FlightSchedule

USAGE_MESSAGE = 'airports.py -i <inputfile> -o <originicao> -u <unitsofdistance>'


def populate_dest_airports(origin, dest_airports, all_airports):
    for airport in all_airports:
        if origin.icao != airport.icao:
            dest_airports.append(airport)


def traverse_airports(dest_airports, previous_airport, origin_icao, units):
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


def total_distance(flights):
    total = 0
    for flight in flights:
        total = total + flight.distance
    return total


def print_flights(flights, units):
    for flight in flights:
        print(flight)
    print(str(int(total_distance(flights))) + units)


def create_flightplan(airports, origin, origin_icao, units):
    flights = traverse_airports(airports, origin, origin_icao, units)
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
    if len(argv) == 0:
        print(USAGE_MESSAGE)
        sys.exit()

    origin_icao = ''
    units = ''

    try:
        opts, args = getopt.getopt(argv, "ho:u:", [])
    except getopt.GetoptError:
        print(USAGE_MESSAGE)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(USAGE_MESSAGE)
            sys.exit()
        elif opt in ("-o", "--origin"):
            origin_icao = arg.strip()
        elif opt in ("-u", "--units"):
            units = arg

    if units == '':
        units = 'km'

    airportService = AirportService()
    airports = airportService.get_airports()

    flightSchedule = FlightSchedule(origin_icao, airports)
    flights = flightSchedule.create_flightplan(units)

    # origin = setup_origin(airports, origin_icao)
    # if origin is None:
    #     print("Unable to find airport with ICAO code: " + origin_icao)
    #     sys.exit()

    # flights = create_flightplan(airports, origin, origin_icao, units)
    print_flights(flights, units)


if __name__ == "__main__":
    main(sys.argv[1:])
