from datetime import datetime


class Ride:

    def __init__(self, bus_id, origin_time: datetime, destination_time: datetime, driver_name: str):
        # Store the id, origin time, destination time, and driver name for the ride
        self.origin_time = origin_time
        self.destination_time = destination_time
        self.__driver_name = driver_name
        self.delays = 0
        self.bus_id = bus_id

    def __str__(self):
        return f'id:{self.bus_id} origin_time:{self.origin_time} destination_time:{self.destination_time} ' \
               f'driver name: {self.__driver_name}'

    def __repr__(self):
        return f'id:{self.bus_id} origin_time:{self.origin_time} destination_time:{self.destination_time}'

    def record_delay(self):
        # Increment the number of delays for the ride
        self.delays += 1