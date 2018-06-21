class Flight(object):
    origin = None
    destination = None
    distance = None
    units = ''

    def __init__(self, origin, destination, distance, units):
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.units = units

    def __str__(self):
        return "-" + self.origin.city + " to " + self.destination.city + \
               " = " + str(int(self.distance)) + " " + self.units
