### Generates the hash table used to hold the package information.
### Adapted from 'Let's Go Hashing', WGU C950 Webinar 1.

### Defines hash table.
class HashTable:
    def __init__(self):
        self.table = []
        size = 41
        for i in range(size):
            self.table.append([])

### Method for adding item to hash table.
    def add(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    ### Method for retrieving information for the hash table.
    def get(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        ### If the key is in the hash table, returns a string containing the information.
        for key_value in bucket_list:
            # print (key_value)
            if key_value[0] == key:
                package_info = str(key_value[1].package_id) + "...." + str(key_value[1].address) + "...." + \
                               str(key_value[1].city) + "...." + str(key_value[1].state) + "...." + \
                               str(key_value[1].zipcode) + "...." + str(key_value[1].deadline) + "...." + \
                               str(key_value[1].weight) + "...." + str(key_value[1].time) + "...." + \
                               str(key_value[1].status)
                return str(package_info)  # value

    ### Method dor returning a package address. Takes a package ID as input.
    def get_address(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                split_details = (str(key_value[1])).split(", ")
                return str(split_details[1])

    ### Method for setting a package delivery time. Takes the package ID and time.
    def set_time(self, key, time):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1].time = time

    ### Gets the delivery time of a package. Takes the package ID.
    def get_time(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1].time

    ### Sets the status of a package. Takes the package ID and status.
    def set_status(self, key, status):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1].status = status

    ### Sets the truck name the package is on. Takes the package ID and the truck name.
    def set_truck(self, key, truck):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            # print (key_value)
            if key_value[0] == key:
                key_value[1].truck = truck

    ### Returns which truck a package is on. Takes the package ID.
    def get_truck(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            # print (key_value)
            if key_value[0] == key:
                return str(key_value[1].truck)
