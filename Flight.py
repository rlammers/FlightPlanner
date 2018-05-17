class Flight(object):
    origin = None
    destination = None
    distance = None

    def __init__(self, origin, destination, distance):
        self.origin = origin
        self.destination = destination
        self.distance = distance

    def __str__(self):
        return "Flight: " + self.origin.icao + " to " + self.destination.icao\
               + " Distance: " + str(int(self.distance)) + "NM"
