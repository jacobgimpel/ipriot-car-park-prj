from abc import ABC, abstractmethod
import random

class Sensor(ABC):
    """
    Abstract base class for sensors. Used for vehicle detection.

    Attributes:
        id (int): Sensor identifier number.
        car_park (CarPark): Car park sensor is registered to.
        is_active (bool): Sensor operation status.
    """
    def __init__(self, id, car_park, is_active=False):
        """
        Initialises sensor with given parameters.

        Args:
            id (int): Sensor identifier number.
            car_park (CarPark): Car park sensor is registered to.
            is_active (bool, optional): Sensor operation status. Default false.
        """
        self.id = id
        self.car_park = car_park
        self.is_active = is_active

    def __str__(self):
        """
        Displays sensor information.

        Returns:
             str: "Sensor at [id], sensor on: [is_active]"
        """
        return f"Sensor {self.id}, sensor on:{self.is_active}"

    @abstractmethod
    def update_car_park(self, plate):
        """
        Abstract method, alerts car park to vehicle entry/exit.

        Args:
            plate (str): Vehicle license plate.
        """
        pass

    def _scan_plate(self):
        """
        Private method to randomly generates license plate. Used for simulation purposes.

        Returns:
            str: License plate in format (example) - "FAKE-370"
        """
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        """
        Detects vehicles and updates car park.
        """
        plate = self._scan_plate()
        self.update_car_park(plate)


class EntrySensor(Sensor):
    """
    Sensor to detect entering vehicles.
    """
    def update_car_park(self, plate):
        """
        Updates car park with plate of the entering vehicle.

        Args:
            plate (str): License plate of entering vehicle.
        """
        self.car_park.add_car(plate)
        print(f"Incoming vehicle detected. Plate {plate}")


class ExitSensor(Sensor):
    """
    Sensor to detect exiting vehicles.
    """
    def update_car_park(self, plate):
        """
        Updates car park, removing the plate.

        Args:
            plate (str): License plate of exiting vehicle.
        """
        self.car_park.remove_car(plate)
        print(f"Outgoing vehicle detected. Plate {plate}")

    def _scan_plate(self):
        """
        Private method. Picks plate at random to simulate a vehicle exiting.

        Returns:
            str: Random license plate from plates list.
        """
        return random.choice(self.car_park.plates)
