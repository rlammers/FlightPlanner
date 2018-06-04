from airports import distance_between, get_airport, read_airports_from_csv
from Airport import Airport


def test_distance_between():
    christchurch = Airport('NZCH', -43.489444, 172.532222, 'Christchurch')
    wellington = Airport('NZWN', -41.327222, 174.805278, 'Wellington')
    auckland = Airport('NZAA', -37.008056, 174.791667, 'Auckland')
    invercargill = Airport('NZNV', -46.412222, 168.312778, 'Invercargill')
    dist = distance_between(christchurch, wellington)
    assert(int(dist) == 164)
    dist = distance_between(wellington, christchurch)
    assert(int(dist) == 164)
    dist = distance_between(christchurch, christchurch)
    assert(int(dist) == 0)
    dist = distance_between(auckland, invercargill)
    assert(int(dist) == 634)


def test_get_airport():
    airports = read_airports_from_csv('airports.csv')
    airport = get_airport('NZAA', airports)
    assert(airport.icao == 'NZAA')
    assert(round(float(getattr(airport, 'latitude')), 6) == -37.008056)
    assert(float(getattr(airport, 'longitude')) == 174.791667)
    assert(getattr(airport, 'city') == 'Auckland')
