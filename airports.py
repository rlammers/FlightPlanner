from geopy import distance
from Airport import Airport
from Flight import Flight

AIRPORTS = [
    Airport('NZCH', -43.489444, 172.532222),
    Airport('NZAA', -37.008056, 174.791667),
    Airport('NZWN', -41.327222, 174.805278),
    Airport('NZQN', -45.021111, 168.739167),
    Airport('NZDN', -45.928056, 170.198333),
    Airport('NZNV', -46.412222, 168.312778),
    Airport('NZHN', -37.866667, 175.331944),
    Airport('NZRO', -38.109167, 176.317222),
    Airport('NZOH', -40.206111, 175.387778),
    Airport('NZWP', -36.787778, 174.630278),
    Airport('NZPM', -40.320556, 175.616944),
    Airport('NZNR', -39.468333, 176.871667),
    Airport('NZTG', -37.673333, 176.197222),
]


def distance_between(dept_airport, arr_airport):
    dept_coords = (dept_airport.latitude, dept_airport.longitude)
    arr_coords = (arr_airport.latitude, arr_airport.longitude)
    return distance.great_circle(dept_coords, arr_coords).nm


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


def populate_dest_airports(origin, dest_airports):
    for airport in AIRPORTS:
        if origin.icao != airport.icao:
            dest_airports.append(airport)


def traverse_airports(dest_airports, previous_airport):
    flights = []
    while len(dest_airports) >= 1:
        close_airport, close_dist = shortest_distance(previous_airport, dest_airports)
        flight = Flight(previous_airport, close_airport, close_dist)
        flights.append(flight)
        previous_airport = close_airport
        dest_airports.remove(close_airport)
    return flights


def return_to_origin(origin, previous_airport):
    dest_airports = [origin]
    close_airport, close_dist = shortest_distance(previous_airport, dest_airports)
    flight = Flight(previous_airport, close_airport, close_dist)

    return flight


def get_airport(icao):
    for airport in AIRPORTS:
        if airport.icao == icao:
            return airport


def main():
    origin_icao = input("Please enter ICAO code for origin: ")
    origin = get_airport(origin_icao)
    previous_airport = origin

    dest_airports = []
    populate_dest_airports(origin, dest_airports)
    flights = traverse_airports(dest_airports, previous_airport)

    final_stop = flights[-1].destination
    return_flight = return_to_origin(origin, final_stop)
    flights.append(return_flight)

    for flight in flights:
        print(flight)


if __name__ == '__main__':
    main()
