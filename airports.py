from geopy import distance

airports = [
            'NZAA',
            'NZWN',
            'NZQN',
            'NZDN',
            'NZNV',
            'NZHN',
            'NZRO',
            'NZOH',
            'NZWP',
            'NZPM',
            'NZNR',
            'NZTG'
            ]

# random.shuffle(airports, random.random)
print(airports)


def distance_between(dept_airport, arr_airport):
    dept_coords = (dept_airport.latitude, dept_airport.longitude)
    arr_coords = (arr_airport.latitude, dept_airport.longitude)
    return distance.great_circle(dept_coords, arr_coords).km


class Airport(object):
    icao = ''
    latitude = 0
    longitude = 0

    def __init__(self, icao, latitude, longitude):
        self.icao = icao
        self.latitude = latitude
        self.longitude = longitude
