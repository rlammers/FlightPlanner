from airports import distance_between, get_airport
from Airport import Airport


def test_distance_between():
    christchurch = Airport('NZCH', -43.489444, 172.532222)
    wellington = Airport('NZWN', -41.327222, 174.805278)
    auckland = Airport('NZAA', -37.008056, 174.791667)
    invercargill = Airport('NZNV', -46.412222, 168.312778)
    dist = distance_between(christchurch, wellington)
    assert(int(dist) == 164)
    dist = distance_between(wellington, christchurch)
    assert(int(dist) == 164)
    dist = distance_between(christchurch, christchurch)
    assert(int(dist) == 0)
    dist = distance_between(auckland, invercargill)
    assert(int(dist) == 634)


def test_get_airport():
    airport = get_airport('NZAA')
    assert(airport.icao == 'NZAA')
    assert(airport.latitude == -37.008056)
    assert(airport.longitude == 174.791667)
