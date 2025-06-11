from abc import ABC, abstractmethod
from random import random
class Sensor(ABC):
    def __init__(self,id,is_active=False,car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"Sensor {self.id}, sensor on:{self.is_active}"

    @abstractmethod
    def update_car_park(self,plate):
        pass

    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0,999), "03d")


class EntrySensor(Sensor):
    def update_car_park(self,plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing vehicle detected. Plate: {plate}")

class ExitSensor(Sensor):
    def _scan_plate(self):
        return random.choice(self.car_park.plates)

