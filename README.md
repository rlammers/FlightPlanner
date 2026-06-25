# FlightPlanner

A flight planning application that generates travel routes between airports. Given a list of airports, it calculates an order to travel between each destination (currently using straight-line paths).

## Features

- **Console Application**: Command-line interface for flight planning
- **Web Service**: RESTful API returning GeoJSON data
- **Geospatial Analysis**: Uses geopy and geographiclib for distance calculations
- **Data Visualization**: Output in GeoJSON format for mapping

## Requirements

- Python 3.13+
- Dependencies managed via pipenv or pip

## Installation

### Using pipenv (recommended)

```bash
pip install pipenv
pipenv install
```

### Using pip

```bash
pip install -r requirements.txt
```

Or install directly:

```bash
pip install pandas geopy geojson bottle pytest coverage
```

## Usage

### Console App

```bash
python flight_planner.py -o "NZCH"
```

Generates a flight plan starting from the specified airport (ICAO code).

### Web Service

```bash
python app.py
```

Starts a local web server on `http://localhost:8080`

#### API Endpoints

- `GET /airports/<icao>` - Get airport information by ICAO code
- `GET /flightschedule` - Get complete flight schedule (flights and airports)
- `GET /flightschedule/airports` - Get airports in the flight schedule
- `GET /flightschedule/flights` - Get flight paths in the schedule
- `GET /flight` - Get sample flight (Christchurch to Auckland)

All endpoints return GeoJSON data. Preview results at [geojson.io](http://geojson.io)

## Testing

Run the test suite:

```bash
pytest -v
```

## Security

All dependencies are kept current with security updates. Dependencies include:

- pandas 3.0.3
- geopy 2.4.1
- geojson 3.3.0
- bottle 0.13.4
- pytest 9.1.1
- coverage 7.14.3

**Note**: This is a demonstration application. Do not expose the web service to untrusted networks without additional security measures (authentication, rate limiting, input validation, HTTPS, etc.).

## Project Structure

- `flight_planner.py` - Main console application
- `app.py` - Web service entry point
- `airport_service.py` - Airport data management
- `flight.py` - Flight route calculations
- `flight_schedule.py` - Flight schedule generation
- `test_*.py` - Unit tests
- `airports.csv` / `small.csv` - Airport data

## Contributing

Issues and pull requests are welcome. Please ensure all tests pass before submitting.
