from Airport import Airport
from geojson import Point, Feature, FeatureCollection

ICAO_INDEX = 1

def test_distance_to():
    units = 'nm'
    christchurch = Airport('NZCH', -43.489444, 172.532222, 'Christchurch')
    wellington = Airport('NZWN', -41.327222, 174.805278, 'Wellington')
    auckland = Airport('NZAA', -37.008056, 174.791667, 'Auckland')
    invercargill = Airport('NZNV', -46.412222, 168.312778, 'Invercargill')
    dist = christchurch.distance_to(wellington, units)
    assert(int(dist) == 164)
    dist = wellington.distance_to(christchurch, units)
    assert(int(dist) == 164)
    dist = christchurch.distance_to(christchurch, units)
    assert(int(dist) == 0)
    dist = auckland.distance_to(invercargill, units)
    assert(int(dist) == 634)
