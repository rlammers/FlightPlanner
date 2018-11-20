from airports import get_airport
from airport import Airport
from airport_service import AirportService


def test_get_airport():
    airport_service = AirportService()
    airports = airport_service.get_airports()
    airport = get_airport('NZAA', airports)
    assert(airport.icao == 'NZAA')
    assert(round(float(getattr(airport, 'latitude')), 6) == -37.008056)
    assert(float(getattr(airport, 'longitude')) == 174.791667)
    assert(getattr(airport, 'city') == 'Auckland')
