from geopy import distance

AIRPORTS = [
    ('NZAA', -37.008056, 174.791667),
    ('NZCH', -43.489444, 172.532222),
    ('NZWN', -41.327222, 174.805278)
    ]
            # 'NZWN',
            # 'NZQN',
            # 'NZDN',
            # 'NZNV',
            # 'NZHN',
            # 'NZRO',
            # 'NZOH',
            # 'NZWP',
            # 'NZPM',
            # 'NZNR',
            # 'NZTG'
            # ]


def distance_between(dept_airport, arr_airport):
    dept_coords = (dept_airport.latitude, dept_airport.longitude)
    arr_coords = (arr_airport.latitude, dept_airport.longitude)
    return distance.great_circle(dept_coords, arr_coords).km


def shortest_distance(dept_airport, destination_airports):
    current_dist = 0
    seen_dist = False
    closest_icao = ''
    min_dist = 0

    for dest in destination_airports:
        if not dept_airport.icao == dest.icao:
            prev_dist = current_dist
            current_dist = distance_between(dept_airport, dest)

            if current_dist < min_dist or not seen_dist:
                closest_icao = dest.icao
                min_dist = current_dist
            seen_dist = True

    print(closest_icao + ' ' + str(min_dist))


class Airport(object):
    icao = ''
    latitude = 0
    longitude = 0

    def __init__(self, icao, latitude, longitude):
        self.icao = icao
        self.latitude = latitude
        self.longitude = longitude


nz_airports = []
for airport in AIRPORTS:
    new_airport = Airport(airport[0], airport[1], airport[2])
    nz_airports.append(new_airport)

shortest_distance(nz_airports[0], nz_airports[1:])
# for nz_airport in nz_airports:
#     print(nz_airport.icao)
