"""
Run the flight planner as a console application.
"""
import argparse

from airport_service import AirportService
from flight import Flight
from flight_schedule import FlightSchedule

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


def create_argument_parser():
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Create a round trip through the airports in airports.csv."
    )
    parser.add_argument(
        '-o',
        '--origin',
        required=True,
        metavar='ICAO',
        help='origin airport ICAO code',
    )
    parser.add_argument(
        '-u',
        '--units',
        choices=('km', 'nm'),
        default='km',
        type=str.lower,
        help='distance units (default: km)',
    )
    return parser


def main(argv=None):
    """Parse command-line arguments and print the resulting flight plan."""
    parser = create_argument_parser()
    args = parser.parse_args(argv)

    airport_service = AirportService()
    airports = airport_service.get_airports()

    try:
        flight_schedule = FlightSchedule(args.origin.strip(), airports)
    except ValueError as error:
        parser.error(str(error))

    flight_schedule.create_flightplan(args.units)
    flight_schedule.print_flights()

    # TODO: Draw flight path lines between the airports for each flight
    # features = flightSchedule.to_geojson()


if __name__ == "__main__":
    main()
