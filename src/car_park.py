from display import Display
from sensor import Sensor
from pathlib import Path
from datetime import datetime
import json


class CarPark:
    """
    Handles vehicles entering and exiting, updates available bays and manages displays/sensors.

    Attributes:
    location (str): Address of the car park.
    capacity (int): Total number of bays in car park.
    plates (list[str]): List of vehicle license plates currently in the carpark. Defaults to [].
    displays (list[Display]): List of displays registered in the carpark. Defaults to [].
    sensors (list[Sesnor]:List of sensors registered in the carpark. Defaults to []
    log_file (Path): File path for logging vehicle entry/exit.
    config_file (Path): File path for storing carpark configuration.
    """
    def __init__(self, location, capacity, plates=None, displays=None, sensors=None, log_file=Path("log.txt"),
                 config_file=Path("config.json")):
        """
        Initialises the CarPark.

        Args:
            location (str): Address of the car park.
            capacity (int): Total number of bays in car park.
            plates (list[str], optional): List of license plates. Defaults to empty list.
            displays (list[Display], optional): Registered displays. Defaults to empty list.
            sensors (list[Sensor], optional): Registered sensors. Defaults to empty list.
            log_file (str/Path, optional): File path for vehicle entry/exit log. Defaults to "log.txt"
            config_file (str/Path, optional): File path for carpark config file. Defaults to "config.json"
        """
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = sensors or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        self.log_file.touch(exist_ok=True)

    def __str__(self):
        """
        Displays CarPark information.

        Returns:
            str: "Car park at [location], with [capacity] bays.
        """
        return f"Car park at {self.location}, with {self.capacity} bays."

    def register(self, component):
        """
        Registers sensor or displays to the carpark.

        Args:
            component (Sensor, Display): Device to be registered.

        Raises:
            TypeError: If component is neither Sensor nor Display.
        """
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)

        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        """
        Records vehicle entering the car park.
        Adds plate value to plates list, updates displays and logs with timestamp.

        Args:
            plate: Vehicle license plate.
        """
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        """
        Records vehicle leaving the car park.
        Removes plate from plates list, updates displays and logs with timestamp.

        Args:
            plate: Vehicle license plate.
        """
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    @property
    def available_bays(self):
        """
        Calculates the current number of available parking bays.

        Returns:
            int: Available bays. Capped at 0 to ensure the number of bays cannot be negative.
        """
        bays_left = self.capacity - len(self.plates)
        return max(0, bays_left)

    def update_displays(self):
        """
        Sends number of available bays and car park temperature to displays.
        Internal temperature set to 25 for demonstration purposes.
        """
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)

    def _log_car_activity(self, plate, action):
        """
        Private method to log vehicle entry/exit to file.
        Logs to file with format:
            "[plate] [action] at [YYYY-MM-DD HH:MM:SS]"

        Args:
            plate (str): Vehicle license plate.
            action (str): Vehicle "entered" or "exited"
        """
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def write_config(self, config_file=None):
        """
        Writes car park configuration to JSON file.
        Configuration saved with parameters location, capacity and log_file (Path).

        Args:
            config_file(str, optional): Optional config_file path. Defaults to config.json.
        """
        json_config = Path(config_file)  if config_file else self.config_file
        with json_config.open("w") as f:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        """
        Creates an instance of CarPark using parameters in config file.

        Args:
            config_file(str, optional): Optional config file path. Defaults to config.json.

        Returns:
            CarPark instance with values from the config file.
        """
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
            return cls(location=config["location"], capacity=config["capacity"], log_file=config["log_file"], config_file=config_file)
