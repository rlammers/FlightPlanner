# FlightPlanner
## Console App
Usage: python flight_planner.py -o "NZCH"

## Web App
Usage: python app.py

### Requests
* Get http://hostname:port/airport/<ICAO>
* Get http://hostname:port/flightschedule

These return GeoJSON, you still need to render that on a map.

You can paste the JSON into a website like http://geojson.io for a preview.

## Dependencies
Use pipenv to install dependencies
