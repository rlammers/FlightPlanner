from Airport import Airport
from geojson import Point, Feature, FeatureCollection

ICAO_INDEX = 1

def test_to_geojson():
    nzch = Airport('NZCH', -43.489444, 172.532222, 'Christchurch')
    point = Point([-43.489444, 172.532222])
    feature = Feature(id=None, geometry=point)
    feature_collection = FeatureCollection(features=[feature])
    assert(nzch.to_geojson() == feature_collection)
