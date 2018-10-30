from bottle import route, run
import Airport

airports = [Airport]

@route('/airports/<name>', method='PUT')
def airport_save(name):
    airports.append(name)


if __name__ == '__main__':
    run(host = 'localhost', port = 8080, debug=True)