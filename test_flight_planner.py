from airport_service import AirportService
from flight_planner import get_airport


def test_get_airport():
    airport_service = AirportService()
    airports = airport_service.get_airports()
    airport = get_airport('NZAA', airports)
    assert(airport.icao == 'NZAA')
    assert(round(float(getattr(airport, 'latitude')), 6) == -37.008056)
    assert(float(getattr(airport, 'longitude')) == 174.791667)
    assert(getattr(airport, 'city') == 'Auckland')
