from airport_service import AirportService

def test_init():
    service = AirportService()
    assert(len(service.airports) == 13)

def test_get_airports():
    service = AirportService()
    airports = service.get_airports()
    assert(len(airports) == 13)

def test_get_airport():
    service = AirportService()
    airport = service.get_airport('NZCH')
    assert(airport.icao == 'NZCH')
    assert(airport.city == 'Christchurch')