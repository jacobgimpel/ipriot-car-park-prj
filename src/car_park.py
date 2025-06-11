from display import Display
from sensor import Sensor
class CarPark:
    def __init__(self, location, capacity, plates=None, displays=None, sensors=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = sensors or []


    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)

        elif not isinstance(component, Display):
            self.displays.append(component)

    def add_car(self,plate):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self,plate):
        self.plates.remove(plate)
        self.update_displays()

    @property
    def available_bays(self):
        if self.plates > max(self.capacity):
            return "0"

    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays: display.update(data)






