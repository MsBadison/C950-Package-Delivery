### Madison Maguire 011029252

import csv
from Package import Package
from HashTable import HashTable
from Truck import Truck
import datetime

### Open Address CSV file and add to a dictionary
### O(n) time, O(n) space
with open("AddressList.csv", "r", encoding="utf-8-sig") as AddressList:
    address_table = {}
    address_csv = csv.reader(AddressList)
    for row in address_csv:
        address_table.__setitem__(row[0], row[2])

### Open Distance CSV file and add to a table
### O(n) time, O(n) space
with open("DistanceList.csv", "r", encoding="utf-8-sig") as DistanceList:
    distance_table = []
    distance_csv = csv.reader(DistanceList)
    for row in distance_csv:
        distance_table.append(row)

### Open Package CSV file and add to a hashtable
### O(n) time, O(n) space
with open("PackageList.csv", "r", encoding="utf-8-sig") as PackageList:
    package_csv = csv.reader(PackageList)
    ### Create hashtable to hold packages
    package_table = HashTable()

    ### Assign values in each row to variables
    for row in package_csv:
        package_id = int(row[0])
        address = row[1]
        city = row[2]
        state = row[3]
        zipcode = row[4]
        deadline = row[5]
        weight = row[6]
        time = datetime.timedelta(hours=8, minutes=0)
        status = "At Hub"
        truck = "truck_1"

        ### Create a package item with the variables in each row
        package_item = Package(package_id, address, city, state, zipcode, deadline, weight, time, status, truck)
        ### Add package item to hashtable, using the package_id as the key
        package_table.add(package_id, package_item)


### Function for looking up the address number. Takes the address as an argument and returns the address number
def address_number(street_address):
    return int(list(address_table.keys())[list(address_table.values()).index(str(street_address))])


### Function for looking up the distance. Takes two addresses as arguments and returns the distance between them.
def distance_lookup(address_1, address_2):
    ### Convert first address to a number using the address_number function
    x = address_number(address_1)
    ### Convert second address to a number using the address_number function
    y = address_number(address_2)
    ### Looks up the distance using the distance_table and assigns it to a variable
    distance = distance_table[x][y]
    return distance


### Create truck objects
### O(n) time, O(n) space
### Truck 1 departs at 8:00.
truck_1 = Truck(16, 18, [2, 7, 8, 10, 13, 14, 15, 16, 19, 20, 21, 23, 24, 29, 34, 37], 0.0,
                "4001 South 700 East", datetime.timedelta(hours=8, minutes=0), "truck_1")
### Truck 2 departs at 9:05.
truck_2 = Truck(16, 18, [1, 3, 4, 5, 6, 40, 18, 22, 26, 27, 30, 31, 33, 35, 36, 38], 0.0, "4001 South 700 East",
                datetime.timedelta(hours=9, minutes=5), "truck_2")
### Truck 3 departure time will be updated later when we know when truck 1 returns.
truck_3 = Truck(16, 18, [9, 11, 12, 17, 25, 28, 32, 39], 0.0, "4001 South 700 East",
                datetime.timedelta(hours=8, minutes=0), "truck_3")

### Create variables for times the first two trucks leave. Truck three will be dependant upon the time truck_1 returns.
truck_1_leave_time = truck_1.time
truck_2_leave_time = truck_2.time


### Create a function for sorting the packages in delivery order using a nearest neighbor algorithm.
### The function also calculates the delivery time of the package.
### The function contains a nested loop, and so is in O(n^2) time.
### The function creates a table of n length as it runs, so its space complexity is O(n).
def sort_packages(truck):
    ### Copy the packages into a temporary list
    package_list = truck.packages.copy()
    ### Create a variable containing the number of packages
    original_list_length = len(truck.packages)
    ### Empty the packages from the truck
    truck.packages = []
    ### Create a while loop that while iterate until all the packages have been loaded

    while len(truck.packages) < original_list_length:
        ### create a variable for the shortest distance and assign a value larger than any distance
        shortest_distance = 9999.9
        ### Create a variable to hold the next package to be loaded
        next_package = 0
        ### Create a loop to iterate over the temporary package list

        for item in package_list:
            ### Set the current distance to the distance between the truck location and the package address
            current_distance = float(distance_lookup(truck.location, package_table.get_address(item)))
            ### Check iof current instance is smaller than the shortest distance so far
            if current_distance < shortest_distance:
                ### If the distance is less, set the next_package variable to the current package
                next_package = item
                ### Set the shortest distance to equal the current distance
                shortest_distance = current_distance

        ### After iterating over the package list, we will now know the package that is to be delivered next
        ### Increase the truck mileage by the distance required to travel to the next package address
        truck.mileage += shortest_distance
        ### Load the next package onto the truck
        truck.packages.append(next_package)
        ### Calculate the time it takes to get to the next address
        delivery_time = datetime.timedelta(hours=shortest_distance / 18)
        ### Set the delivery time of the package by adding the time it takes to do the delivery to the time on the truck
        package_table.set_time(next_package, (truck.time + delivery_time))
        ### Update the truck time to the time when the package is delivered
        truck.time = (truck.time + delivery_time)
        ### Update the truck location to the address of the delivered package
        truck.location = package_table.get_address(next_package)
        ### Update the truck the package is on
        package_table.set_truck(next_package, truck.name)
        ### Remove the delivered package form the temporary package list
        package_list.remove(next_package)


### Sort the package for the first two trucks. We need to know when truck one returns to the hub to set truck three's
### departure time.
sort_packages(truck_1)
sort_packages(truck_2)

### Get the time truck one is finished delivering packages
truck_1_last_time = package_table.get_time(truck_1.packages[-1])
### Get the distance from truck one's last delivery back to the hub
truck_1_hub_distance = distance_lookup(package_table.get_address(truck_1.packages[-1]), "4001 South 700 East")
### Set truck three's time to the time truck one returns to the hub
truck_3.time = truck_1_last_time + datetime.timedelta(hours=float(truck_1_hub_distance) / 18)
### Update the time truck three will leave the hub
truck_3_leave_time = truck_3.time
### Sort the packages Out for delivery three
sort_packages(truck_3)

### Calculate the total milage by adding the distance the three trucks travel, and adding the distance truck one must
### travel back to the hub in order to puck up truck three.
total_mileage = int(truck_1.mileage + float(truck_1_hub_distance) + truck_2.mileage + truck_3.mileage)

### This is the user interface
print("Welcome to WGUPS!\nThe total distance traveled by our trucks today will be " + str(total_mileage) + " miles.\n")
### Create variable to hold the user's choice
user_option = 0
### Create a while loop that will run until the user selects option 3 to exit.
while user_option != "3":
    ### Get the time the user would like to look up and assign to a variable
    user_time = input("Please enter a time you'd like to look up in HHMM format.\n>")
    ### If the user enters an invalid time, this while loop will run until they enter a valid time.

    while int(user_time) > 2359 or len(user_time) < 4:
        user_time = input("Please enter a valid time in HHMM format.\n>")

    ### Extract the number of hours from the entered time.
    user_hours = int(int(user_time) / 100)
    ### Extract the number of minutes form the entered time.
    user_minutes = int(int(user_time) % 100)
    ### Set the user time to a time object using the extracted hours and minutes.
    user_time = datetime.timedelta(hours=int(user_hours), minutes=int(user_minutes))
    print("Selected time is " + str(user_time))

    ### Ask the user if they would like to look up a single package, all packages, or quit
    user_option = input("1. Look up single package.\n2. Look up all packages.\n3. Quit.\n>")

    ### If the user selects option 1, ask what package id they would like to look up.
    if user_option == "1":
        user_package = input("Enter a valid package ID\n>")
        ### Create a while loop that will run until the user enters a valid package id.
        while int(user_package) > 40 or int(user_package) < 1:
            user_package = input("Not a valid package ID\n>")

        ### If the time is after the delivery time, update the status to delivered.
        if user_time > package_table.get_time(int(user_package)):
            package_table.set_status(int(user_package), "Delivered")

        ### If the package is on truck one and the entered time is before the delivery time, update the status if
        ### the truck has departed.
        elif package_table.get_truck(int(user_package)) == "truck_1" and user_time < \
                package_table.get_time(int(user_package)):
            if user_time > truck_1_leave_time:
                package_table.set_status(int(user_package), "Out for delivery")

        ### If the package is on truck two, update the status if the truck has departed.
        elif package_table.get_truck(int(user_package)) == "truck_2" and package_table.get_time(
                int(user_package)) > user_time > truck_2_leave_time:
            package_table.set_status(int(user_package), "Out for delivery")

        ### If the package is on truck three, update the status if the truck has departed.
        elif package_table.get_truck(int(user_package)) == "truck_3" and package_table.get_time(
                int(user_package)) > user_time > truck_3_leave_time:
            package_table.set_status(int(user_package), "Out for delivery")
        print("Package ID....Address....City....State....Zipcode....Deadline....Weight....Expected "
              "Delivery....Time....Status\n")
        print(package_table.get(int(user_package)) + "\n")

    ### If the user selects option 2, print a list of all the packages
    elif user_option == "2":
        print("Package ID....Address....City....State....Zipcode....Deadline....Weight....Expected "
              "Delivery....Time....Status\n")
        ### Update the status and print the packages on truck one.
        for item in truck_1.packages:
            if user_time > truck_1_leave_time:
                package_table.set_status(item, "Out for delivery")
            if user_time > package_table.get_time(item):
                package_table.set_status(item, "Delivered")
            print(package_table.get(item))

        ### Update the status and print the packages on truck two.
        for item in truck_2.packages:
            if user_time > truck_2_leave_time:
                package_table.set_status(item, "Out for delivery")
            if user_time > package_table.get_time(item):
                package_table.set_status(item, "Delivered")
            print(package_table.get(item))

        ### Update the status and print the packages on truck three.
        for item in truck_3.packages:
            if user_time > truck_3_leave_time:
                package_table.set_status(item, "Out for delivery")
            if user_time > package_table.get_time(item):
                package_table.set_status(item, "Delivered")
            print(package_table.get(item))
        print("\n")

    ### If the user selects option 3, quit the program.
    elif user_option == "3":
        print("Thank you for using WGUPS. Have a great day!")
        quit()

    ### Prompts the user to enter the option again if the input was not valid.
    else:
        user_option = input("Invalid option!\n1. Look up single package.\nLook up all packages\n3. Quit\n>")
