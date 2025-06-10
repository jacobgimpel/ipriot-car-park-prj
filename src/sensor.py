class Sensor:
    def __init__(self,id,is_active=False,car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"Sensor {self.id}, sensor on:{self.is_active}"

class EntrySensor(Sensor):
    ...

class ExitSensor(Sensor):
    ...

