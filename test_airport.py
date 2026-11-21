"""Unit tests for the Airport model."""

import pytest

from airport import Airport


@pytest.fixture(name='christchurch')
def christchurch_fixture():
    """Return Christchurch International Airport."""
    return Airport('NZCH', -43.489444, 172.532222, 'Christchurch')


@pytest.fixture(name='wellington')
def wellington_fixture():
    """Return Wellington International Airport."""
    return Airport('NZWN', -41.327222, 174.805278, 'Wellington')


def test_initialization(christchurch):
    """Airport attributes are populated from the constructor arguments."""
    assert christchurch.icao == 'NZCH'
    assert christchurch.latitude == -43.489444
    assert christchurch.longitude == 172.532222
    assert christchurch.city == 'Christchurch'


def test_to_geojson(christchurch):
    """An airport is represented by a GeoJSON point with its city."""
    feature = christchurch.to_geojson()

    assert feature['type'] == 'Feature'
    assert feature['geometry']['type'] == 'Point'
    assert feature['geometry']['coordinates'] == [172.532222, -43.489444]
    assert feature['properties'] == {'city': 'Christchurch'}


@pytest.mark.parametrize(
    ('units', 'expected'),
    [
        ('nm', 164.0),
        ('NM', 164.0),
        ('km', 304.0),
    ],
)
def test_distance_to_returns_requested_units(christchurch, wellington, units, expected):
    """Great-circle distances are returned in nautical miles or kilometres."""
    assert christchurch.distance_to(wellington, units) == pytest.approx(expected, abs=1)


def test_distance_to_same_airport_is_zero(christchurch):
    """The distance from an airport to itself is zero."""
    assert christchurch.distance_to(christchurch, 'nm') == pytest.approx(0)


def test_distance_to_rejects_invalid_units(christchurch, wellington):
    """Unsupported distance units produce a clear error."""
    with pytest.raises(ValueError, match='Invalid unit specified'):
        christchurch.distance_to(wellington, 'miles')


def test_closest_airport_returns_nearest_candidate(christchurch, wellington):
    """The nearest airport is selected from the supplied candidates."""
    auckland = Airport('NZAA', -37.008056, 174.791667, 'Auckland')
    invercargill = Airport('NZNV', -46.412222, 168.312778, 'Invercargill')

    closest = christchurch.closest_airport(
        [auckland, invercargill, wellington],
        'nm',
    )

    assert closest is wellington


def test_closest_airport_excludes_matching_icao(christchurch, wellington):
    """An airport is not considered its own closest destination."""
    duplicate = Airport('NZCH', -43.0, 172.0, 'Duplicate Christchurch')

    assert christchurch.closest_airport([duplicate, wellington], 'km') is wellington


@pytest.mark.parametrize('airports', [[], [Airport('NZCH', 0, 0, 'Duplicate')]])
def test_closest_airport_returns_none_without_candidates(christchurch, airports):
    """No result is returned when there are no eligible candidates."""
    assert christchurch.closest_airport(airports, 'nm') is None
