from bottle import route, run
from airport_service import AirportService
from Airport import Airport

airport_service = None

@route('/airports/<icao>', method='GET')
def get_airport(icao):
   airport = airport_service.get_airport(icao)
   return airport.to_geojson()


if __name__ == '__main__':
    airport_service = AirportService()
    run(host = 'localhost', port = 8080, debug=True)