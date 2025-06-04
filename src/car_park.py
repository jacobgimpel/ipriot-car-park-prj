class CarPark:
    def __init__(self, location = unknown, capacity = 0, plates = None, sensors = None, displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates
        self.sensors = sensors or []
        self.displays = displays

    def __str__(self):
        return f"{self.location} has capacity of {self.capacity}"

