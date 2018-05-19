from geopy import distance
from Airport import Airport
from Flight import Flight


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


def populate_dest_airports(origin, dest_airports, all_airports):
    for airport in all_airports:
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


def get_airport(icao, airports):
    for airport in airports:
        if airport.icao == icao:
            return airport


def total_distance(flights):
    total = 0
    for flight in flights:
        total = total + flight.distance
    return total


def read_airports_from_csv(csv_file):
    airports = []
    with open(csv_file, 'r') as f:
        for line in f:
            line_array = line.rstrip().split(',')
            airport = Airport(line_array[0], line_array[1], line_array[2].rstrip())
            airports.append(airport)
    return airports


def main():
    airports = read_airports_from_csv('airports.csv')

    origin_icao = input("Please enter ICAO code for origin: ")
    origin = get_airport(origin_icao, airports)
    previous_airport = origin

    dest_airports = []
    populate_dest_airports(origin, dest_airports, airports)
    flights = traverse_airports(dest_airports, previous_airport)

    final_stop = flights[-1].destination
    return_flight = return_to_origin(origin, final_stop)
    flights.append(return_flight)

    for flight in flights:
        print(flight)

    print(str(int(total_distance(flights))) + "NM")


if __name__ == '__main__':
    main()
