class Flight(object):
    origin = None
    destination = None
    distance = None

    def __init__(self, origin, destination, distance):
        self.origin = origin
        self.destination = destination
        self.distance = distance

    def __str__(self):
        return "-" + self.origin.city + " to " + self.destination.city + \
               " = " + str(int(self.distance)) + "NM"
