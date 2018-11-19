"""
This is a bottle app to run the airport and flight planner services
"""
from bottle import route, run
from airport_service import AirportService
from flight_schedule import FlightSchedule

AIRPORT_SERVICE = None


@route('/airports/<icao>', method='GET')
def get_airport(icao):
    """
    Get an airport from the airport service by passing an ICAO code
    """
    airport = AIRPORT_SERVICE.get_airport(icao)
    return airport.to_geojson()


@route('/flightschedule', method='GET')
def get_flightschedule():
    """
    Get a flight schedule, currently hardcoded to use NZCH and a list of NZ airports.
    To be extended to work with any in the future.
    """
    airports = AIRPORT_SERVICE.get_airports()
    schedule = FlightSchedule('NZCH', airports)
    schedule.create_flightplan('km')
    return schedule.to_geojson()


if __name__ == '__main__':
    AIRPORT_SERVICE = AirportService()
    run(host='localhost', port=8080, debug=True)
