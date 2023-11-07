### Creates a package object containing package information.

class Package:
    def __init__(self, package_id, address, city, state, zipcode, deadline, weight, time, status, truck):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.time = time
        self.status = status
        self.truck = truck

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.package_id, self.address, self.city, self.state, self.zipcode, self.deadline,
            self.weight, self.time, self.status)
