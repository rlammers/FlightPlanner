from geopy import distance
from Airport import Airport

AIRPORTS = [
    ('NZCH', -43.489444, 172.532222),
    ('NZAA', -37.008056, 174.791667),
    ('NZWN', -41.327222, 174.805278),
    ('NZQN', -45.021111, 168.739167),
    ('NZDN', -45.928056, 170.198333),
    ('NZNV', -46.412222, 168.312778),
    ('NZHN', -37.866667, 175.331944),
    ('NZRO', -38.109167, 176.317222),
    ('NZOH', -40.206111, 175.387778),
    ('NZWP', -36.787778, 174.630278),
    ('NZPM', -40.320556, 175.616944),
    ('NZNR', -39.468333, 176.871667),
    ('NZTG', -37.673333, 176.197222),
]


def distance_between(dept_airport, arr_airport):
    dept_coords = (dept_airport.latitude, dept_airport.longitude)
    arr_coords = (arr_airport.latitude, arr_airport.longitude)
    return distance.great_circle(dept_coords, arr_coords).km


def shortest_distance(dept_airport, destination_airports):
    seen_dist = False
    closest_airport = None
    min_dist = 0

    for dest in destination_airports:
        if not dept_airport.icao == dest.icao:
            current_dist = distance_between(dept_airport, dest)

            if current_dist < min_dist or not seen_dist:
                closest_airport = dest
                min_dist = current_dist
            seen_dist = True

    return closest_airport, min_dist


def populate_dest_airports(dest_airports):
    for airport in AIRPORTS:
        new_airport = Airport(airport[0], airport[1], airport[2])
        dest_airports.append(new_airport)


def traverse_airports(dest_airports, previous_airport):
    while len(dest_airports) >= 1:
        close_airport, close_dist = shortest_distance(previous_airport, dest_airports)
        print('Dept: ' + previous_airport.icao + " Dest: " + close_airport.icao + " " + str(int(close_dist)) + " nm")
        previous_airport = close_airport
        dest_airports.remove(close_airport)
    return previous_airport


def return_to_origin(dest_airports, origin, previous_airport):
    dest_airports.append(origin)
    close_dist = shortest_distance(previous_airport, dest_airports)
    print('Dept: ' + previous_airport.icao + " Dest: " + origin.icao + " " + str(int(close_dist[1])) + " nm")


def get_airport(icao):
    for airport in AIRPORTS:
        if airport[0] == icao:
            return Airport(airport[0], airport[1], airport[2])
    return None


def main():
    origin_icao = input("Please enter ICAO code for origin:")
    origin = get_airport(origin_icao)
    previous_airport = origin

    dest_airports = []
    populate_dest_airports(dest_airports)
    previous_airport = traverse_airports(dest_airports, previous_airport)

    return_to_origin(dest_airports, origin, previous_airport)


if __name__ == '__main__':
    main()
