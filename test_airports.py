from airports import distance_between
from Airport import Airport


def test_distance_between():
    christchurch = Airport('NZCH', -43.489444, 172.532222)
    wellington = Airport('NZWN', -41.327222, 174.805278)
    dist = distance_between(christchurch, wellington)
    assert(int(dist) == 304)
    dist = distance_between(wellington, christchurch)
    assert(int(dist) == 304)
    dist = distance_between(christchurch, christchurch)
    assert(int(dist) == 0)
