from BusCompany import BestBusCompany
import pickle
from datetime import datetime
import pprint


class Menu:
    manager_options = {1: 'add route', 2: 'delete route', 3: 'update route',
                       4: 'add scheduled ride', 5: 'view routes',
                       6: 'exit'}

    passenger_options = {1: 'search route', 2: 'report delay', 3: 'exit'}

    def __init__(self, bus_company):
        self.bus_company = bus_company

    def password_manager(self):
        count = 0
        while count < 3:
            password = input("please enter password:")
            if password == 'RideWithUs':
                print('=============================================')
                print("correct password you have access as a manager")
                print('=============================================')
                break
            elif password != 'RideWithUs':
                count += 1
                print('=============================================')
                print(f"wrong password you have {3 - count} more tries")
                print('=============================================')
                continue
        if count == 3:
            print('=============================================')
            print("you entered wrong password 3 times, bye-bye!")
            print('=============================================')
            with open('bus_company.pickle', 'wb') as fh:
                pickle.dump(self.bus_company, fh)
                print('Saved company database!')
            exit()

    def run(self):
        print('=============================================')
        print("======== Welcome to Best Bus Ever! ==========")
        print('=============================================')
        while True:
            selection = int(
                input(f"Please select one of the following options:\n 1: Manager\n 2. Passenger\n 3. Exit\n"))
            if selection not in [1, 2, 3]:
                print("Wrong input please select from options")
                continue
            break
        if selection == 1:
            self.password_manager()

            while True:
                pprint.pprint(self.manager_options)
                action = int(input("please choose from options"))
                if action not in self.manager_options:
                    print(f"choose from Manager options only")
                    continue
                if action == 1:
                    while True:
                        # The user selected the "Add Route" option
                        # Get the line number, origin, destination, and stops for the new route
                        print('=============================================')
                        line_number = input("Enter line number: ")
                        if not line_number.isdigit():
                            print('=============================================')
                            print("Enter line number as numbers")
                            continue
                        line_number = int(line_number)
                        if line_number in self.bus_company.routes:
                            print('=============================================')
                            print("number already taken enter different number")
                            continue
                        print('=============================================')
                        origin = input("Enter the origin: ")
                        destination = input("Enter the destination: ")
                        stops = input("Enter the stops (separated by commas): ")
                        stops = stops.split(",")
                        print('=============================================')

                        # Add the new route to the company
                        # Add the new route to the company
                        self.bus_company.add_route(line_number, origin, destination, stops)
                        print('=============================================')
                        print(
                            f"Route: line number: {line_number} from {origin} to {destination} "
                            f"with stops: {stops} added successfully")
                        print('=============================================')
                        break
                elif action == 2:
                    print('=============================================')
                    line_number = input("Enter line number: ")
                    if not line_number.isdigit():
                        print('=============================================')
                        print("Enter line number as numbers")
                        return
                    line_number = int(line_number)
                    if line_number not in self.bus_company.routes:
                        print('=============================================')
                        print("Route does not exist")
                        return
                    print('=============================================')
                    confirm = input("Are you sure you want to delete this route? Type 'yes' to confirm: ")
                    if confirm.lower() != 'yes':
                        print('=============================================')
                        print("Route not deleted")
                        return
                    # Delete the route from the company
                    self.bus_company.delete_route(line_number)
                    print('=============================================')
                    print(f"Route: line number: {line_number} deleted successfully")
                    print('=============================================')
                elif action == 3:
                    # The user selected the "Update Route" option
                    # Get the line number of the route to update
                    print('=============================================')
                    line_number = input("Enter line number: ")
                    if not line_number.isdigit():
                        print('=============================================')
                        print("Enter line number as numbers")
                        continue
                    line_number = int(line_number)
                    if line_number not in self.bus_company.routes:
                        print('=============================================')
                        print("Route does not exist")
                        continue
                    # Get the new origin, destination, and stops for the route
                    print('=============================================')
                    origin = input("Enter the new origin: ")
                    destination = input("Enter the new destination: ")
                    stops = input("Enter the new stops (separated by commas): ")
                    stops = stops.split(",")
                    # Update the route in the company
                    self.bus_company.update_route(line_number, origin, destination, stops)
                    print('=============================================')
                    print(f"Route: line number: {line_number} updated successfully")
                    print('=============================================')
                elif action == 4:
                    # The user selected the "Add Scheduled Ride" option
                    # Get the line number, date, and time for the new scheduled ride
                    print('=============================================')
                    line_number = input("Enter line number: ")
                    if not line_number.isdigit():
                        print('=============================================')
                        print("Enter line number as numbers")
                        continue
                    line_number = int(line_number)
                    if line_number not in self.bus_company.routes:
                        print('=============================================')
                        print("Route does not exist")
                        continue
                    date = input("Enter the date (yyyy-mm-dd): ")
                    origin_time = input("Enter the time (hh:mm): ")
                    destination_time = input("Enter the time (hh:mm): ")
                    driver_name = input("Enter drivers name:")
                    # Add the new scheduled ride to the company
                    self.bus_company.add_scheduled_ride(line_number, date, origin_time, destination_time, driver_name)
                    print('=============================================')
                    print(f"Scheduled ride on route: line number: {line_number} on {date} will leave"
                          f" at {origin_time} and will arrive at : {destination_time} ")
                    print('=============================================')
                elif action == 5:
                    # The user selected the "View Routes" option
                    # Print the routes in the company
                    print('=============================================')
                    print("Routes:")
                    for line_number, route in self.bus_company.routes.items():
                        print(f"Line number: {line_number} - {route}")
                    print('=============================================')
                elif action == 6:
                    # The user selected the "Exit" option
                    # Save the company object to a file and exit
                    with open('bus_company.pickle', 'wb') as fh:
                        pickle.dump(self.bus_company, fh)
                        print('Saved company database!')
                    print('Exiting program...')
                    exit()

        if selection == 2:
            while True:
                pprint.pprint(self.passenger_options)
                action = int(input("please choose from options"))
                if action not in self.passenger_options:
                    print(f"choose from Passenger options only")
                    continue
                if action == 1:
                    while True:
                        xxx = int(input("choose what to search:\n"
                                        "1. search by origin\n"
                                        "2. search by destination\n"
                                        "3. search by stops\n"
                                        "4. search route by line number\n"))

                        if xxx in [1, 2, 3, 4]:
                            if 1:
                                # Get the origin for the route
                                print('=============================================')
                                origin = input("Enter the origin: ")

                                # Search for routes from the company
                                routes = self.bus_company.search_origin(origin)

                                if not routes:
                                    print('=============================================')
                                    print("No routes found")
                                else:
                                    # Print the found routes
                                    print('=============================================')
                                    print("Routes:")
                                    for line_number in routes:
                                        print(f"Line number: {line_number}")
                            elif 2:
                                # Get the destination for the route
                                print('=============================================')
                                destination = input("Enter the origin: ")

                                # Search for routes from the company
                                routes = self.bus_company.search_destination(destination)

                                if not routes:
                                    print('=============================================')
                                    print("No routes found")
                                else:
                                    # Print the found routes
                                    print('=============================================')
                                    print("Routes:")
                                    for line_number in routes:
                                        print(f"Line number: {line_number}")
                            elif 3:
                                # Get the stop for the route
                                print('=============================================')
                                stop = input("Enter the stop: ")

                                # Search for routes from the company
                                routes = self.bus_company.search_stops(stop)

                                if not routes:
                                    print('=============================================')
                                    print("No routes found")
                                else:
                                    # Print the found routes
                                    print('=============================================')
                                    print("Routes:")
                                    for line_number in routes:
                                        print(f"Line number: {line_number}")
                            elif 4:
                                # The user selected the "Search Route" option
                                print('=============================================')
                                line_number = input("Enter the line number: ")
                                if not line_number.isdigit():
                                    print('=============================================')
                                    print("Enter line number as numbers")

                                # Search for the route from the company
                                route = self.bus_company.search_route(line_number=int(line_number))

                                if route is None:
                                    print('=============================================')
                                    print("Route not found")
                                else:
                                    # Print the details of the route
                                    print('=============================================')
                                    print(f"Line number: {route.line_number}")
                                    print(f"Origin: {route.origin}")
                                    print(f"Destination: {route.destination}")
                                    if route.stops:
                                        print(f"Stops: {', '.join(route.stops)}")
                                    else:
                                        print('Direct ride')

                elif action == 2:
                    while True:
                        # The user selected the "Report Delay" option
                        # Get the line number of the delayed route
                        print('=============================================')
                        line_number = input("Enter line number: ")
                        if not line_number.isdigit():
                            print('=============================================')
                            print("Enter line number as numbers")
                            continue
                        line_number = int(line_number)
                        if line_number not in self.bus_company.routes:
                            print('=============================================')
                            print("Route does not exist")
                            continue
                    self.bus_company.report_delay(line_number)
                    print('=============================================')
                    print(f"Delay on route: line number: {line_number} reported successfully")
                    print('=============================================')

                elif action == 3:
                    # The user selected the "Exit" option
                    # Save the company object to a file and exit
                    with open('bus_company.pickle', 'wb') as fh:
                        pickle.dump(self.bus_company, fh)
                        print('Saved company database!')
                    print('Exiting program...')
                    exit()
