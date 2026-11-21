# FlightPlanner

A flight planning application that generates a round trip through the airports in
`airports.csv`. Starting from a selected airport, it repeatedly chooses the nearest
unvisited airport using great-circle distance, then returns to the origin.

## Features

- **Console application**: Prints each flight leg and the total route distance
- **Web service**: Bottle endpoints that return airport and flight data as GeoJSON
- **Distance calculation**: Uses geopy to calculate great-circle distances
- **GeoJSON output**: Produces features suitable for use with mapping tools

## Requirements

- Python 3.13
- pipenv (recommended) or pip

## Installation

### Using pipenv (recommended)

```bash
python -m pip install pipenv
pipenv install
pipenv shell
```

### Using pip

```bash
python -m pip install pandas geopy geojson bottle pytest coverage pylint
```

## Usage

### Console App

```bash
python flight_planner.py -o "NZCH"
```

Generates a round trip starting from the specified airport. The ICAO code must be
present in `airports.csv`.

#### Console switches

| Switch | Description |
| --- | --- |
| `-h`, `--help` | Display the usage message and exit. |
| `-o <ICAO>`, `--origin <ICAO>` | Set the required origin airport using its ICAO code, for example `NZCH`. |
| `-u <units>`, `--units <units>` | Set the distance units to `km` or `nm`. Defaults to `km`. |

For example, to generate a flight plan from Auckland with distances in nautical miles:

```bash
python flight_planner.py -o "NZAA" -u "nm"
```

### Web Service

```bash
python app.py
```

Starts Bottle's development server at `http://localhost:8080`.

#### API Endpoints

- `GET /airports/<icao>` - Get an airport by ICAO code
- `GET /flightschedule` - Get the airports and flight paths in the schedule
- `GET /flightschedule/airports` - Get the schedule's airports
- `GET /flightschedule/flights` - Get the schedule's flight paths
- `GET /flight` - Get a sample flight path from Christchurch to Auckland

The schedule endpoints currently use Christchurch (`NZCH`) as the origin and
kilometres as the distance unit. Successful responses are GeoJSON and can be
previewed at [geojson.io](https://geojson.io/).

## Testing

Run the test suite:

```bash
python -m pytest -v
```

## Security considerations

**Note**: This is a demonstration application. Do not expose the web service to untrusted networks without additional security measures (authentication, rate limiting, input validation, HTTPS, etc.).

## Project Structure

- `flight_planner.py` - Main console application
- `app.py` - Web service entry point
- `airport.py` - Airport model and distance calculations
- `airport_service.py` - Airport data management
- `flight.py` - Flight route calculations
- `flight_schedule.py` - Flight schedule generation
- `test_*.py` - Unit tests
- `airports.csv` / `small.csv` - Airport data
- `Pipfile` / `Pipfile.lock` - Dependency declarations and lock data

## Contributing

Issues and pull requests are welcome. Please ensure all tests pass before submitting.
