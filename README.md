# FlightPlanner
This is not a real flight planner. Currently it doesn't have any routes just a straight line between airports. It is based around given a list of airports, return a order to travel between each destination.

## Security
No consideration has been given to the security of the webservice. It is NOT recommended to host this on any server exposed to the internet. Feel free to raise any issues or send pull requests.

## Console App
Usage: python flight_planner.py -o "NZCH"

## Web Service
Usage: python app.py

### Requests
* Get http://hostname:port/airport/icao
* Get http://hostname:port/flightschedule

These return GeoJSON, you still need to render that on a map.

You can paste the JSON into a website like http://geojson.io for a preview.

## Dependencies
Use pipenv to install dependencies
