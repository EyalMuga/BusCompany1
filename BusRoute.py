class BusRoute:
    def __init__(self, line_number: int, origin: str, destination: str, stops: list[str]):
        self.rides = []
        self.bus_route: {line_number: [origin, destination, stops]} = {}
        self._line_number = line_number
        self.origin = origin
        self.destination = destination
        self.stops = stops

    def __str__(self):
        return f'line_number: {self._line_number} \n origin: {self.origin} \n destination: {self.destination} \n' \
               f' list_stops: {self.stops} \n bus_schedule: {self.rides}'

    def add_scheduled_ride(self, ride):
        # Store the scheduled ride in the route
        self.rides.append(ride)

    def view_rides(self):
        print(self.rides)

    def delete_scheduled_ride(self, ride_id: int):
        try:
            ride = next(ride for ride in self.rides if ride.id == ride_id)
        except StopIteration:
            # No ride was found with a matching id
            ride = None

        # Remove the scheduled ride from the route
        self.rides.remove(ride)
