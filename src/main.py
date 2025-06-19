from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

car_park = CarPark("Moondalup", 100, log_file="moondalup.txt")

car_park.write_config("moondalup_config.json")

car_park = CarPark.from_config("moondalup_config.json")

entry_sensor = EntrySensor(1, car_park, True)

exit_sensor = ExitSensor(2, car_park, True)

display = Display(1, car_park, "Welcome to Moondalup", True)


print("Cars entering:")
for i in range (10):
    entry_sensor.detect_vehicle()

print("\nCars exiting")
for i in range(2):
    exit_sensor.detect_vehicle()






