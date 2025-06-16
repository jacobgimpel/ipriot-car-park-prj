import unittest
from sensor import Sensor, EntrySensor, ExitSensor
from car_park import CarPark


class TestEntrySensor(unittest.TestCase):

    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.entry_sensor = EntrySensor(1, self.car_park)

    def test_entry_sensor_initialized(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertEqual(self.entry_sensor.car_park, self.car_park)

    def test_detect_vehicle(self):
        self.entry_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), 1)


class TestExitSensor(unittest.TestCase):

    def setUp(self) -> None:
        self.car_park = CarPark("123 Example Street", 100)
        self.exit_sensor = ExitSensor(1, self.car_park)
        self.entry_sensor = EntrySensor(1, self.car_park)

    def test_exit_sensor_initialized(self):
        self.assertIsInstance(self.exit_sensor, ExitSensor)
        self.assertEqual(self.exit_sensor.id, 1)
        self.assertEqual(self.exit_sensor.car_park, self.car_park)

    def test_detect_vehicle(self):
        self.entry_sensor.detect_vehicle()
        self.exit_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), 0)
