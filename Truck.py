### Creates a truck object containing truck information.

class Truck:

    def __init__(self, capacity, speed, packages, mileage, location, time, name):
        self.capacity = capacity
        self.speed = speed
        self.packages = packages
        self.mileage = mileage
        self.location = location
        self.time = time
        self.name = name

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.packages, self.mileage, self.location,
                                           self.time)
