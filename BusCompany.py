from datetime import datetime
from random import random
from BusRoute import BusRoute
from ScheduledRide import Ride


class BestBusCompany:
    # A class that represents the Best Bus Ever company
    def __init__(self):
        self.routes = {}
        self.rides = []

    def __str__(self):
        return self.routes, self.rides

    def view_routes(self):
        if not self.routes:
            print("There are no routes.")
            return

        for line_number, route in self.routes.items():
            self.origin = route.origin
            self.destination = route.destination
            self.stops = route.stops

            print(f"Line number: {line_number}")
            print(f"Origin: {self.origin}")
            print(f"Destination: {self.destination}")
            if self.stops:
                print(f"Stops: {', '.join(self.stops)}")
            else:
                print('Direct ride')

    def add_route(self, line_number: int, origin: str, destination: str, stops: list[str]):
        if line_number in self.routes:
            return False
        self.routes[line_number] = BusRoute(line_number, origin, destination, stops)

    def delete_route(self, line_number: int):
        # Method to delete a bus route from the company

        # Check if the given line number exists in the company's routes dictionary
        if line_number in self.routes:
            # Delete the route from the dictionary
            del self.routes[line_number]

    def update_route(self, line_number: int, origin: str = None, destination: str = None, stops: list[str] = None):
        self.routes[line_number] = BusRoute(line_number, origin, destination, stops)

    def add_scheduled_ride(self, line_number: int, date: datetime, origin_time: datetime, destination_time: datetime,
                           driver_name: str):
        # Check if the given line number exists in the company's routes dictionary
        if line_number in self.routes:
            # Get the route object for the given line number
            route = self.routes[line_number]

            bus_id = int(random() * 1000)

            # Create a new ScheduledRide object with the given id, origin time, destination time, and driver name
            ride = Ride(bus_id, origin_time, destination_time, driver_name)

            # Add the scheduled ride to the route
            route.add_scheduled_ride(ride)

    def search_station(self, station) -> list:
        stops_list = []
        for line in self.routes:
            if self.routes[line].search_station(station):
                stops_list.append(line)
        return stops_list

    # searches for origin and returns list of lines that include this origin:
    def search_origin(self, origin) -> list:
        origin_list = []
        for line in self.routes:
            if self.routes[line].search_origin(origin):
                origin_list.append(line)
        return origin_list

    # searches for destination and returns list of lines that include this destination:
    def search_destination(self, destination) -> list:
        destination_list = []
        for line in self.routes:
            if self.routes[line].search_destination(destination):
                destination_list.append(line)
        return destination_list

    def search_route(self, line_number: int):
        # Check if the given line number exists in the company's routes dictionary
        if line_number in self.routes:
            # Return the route object for the given line number
            return self.routes[line_number]
        else:
            # Return None if the route is not found
            return None

    def report_delay(self, bus_id):
        for route in self.routes:
            # Loop through all the rides in the current route
            for ride in route.rides:
                # Check if the ride ID matches the specified ride id
                if ride[bus_id] == ride[bus_id]:
                    # Record the delay for the ride
                    ride.delays += 1
