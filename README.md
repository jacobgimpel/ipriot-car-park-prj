# IP4RiOT Assessment 3 -  Moondalup Car Park System

The Car Park is a prototype smart car park management program developed in Python, for the city of Moondalup.
The program has been written to meet requirements specified by the city's Chief Technology Officer. 
Car Park functions by using sensors and displays to send information to and from the central management system (the Car Park)
The program is able to:

- Use sensors to track the number of incoming/outgoing vehicles and log their license plate in real-time
- Use displays to show the temperature of the car park, announcements and number of vacant bays
- Store vehicle license plates to a file, with time-stamps
- Save and load a car park configuration from a .JSON file

# Installation

Step 1:

using git,create a local clone of the repository on your machine:

```bash
git clone https://github.com/jacobgimpel/ipriot-car-park-prj
```

Step 2:

Open the repository in your IDE of choice (e.g, PyCharm)

# Usage Guide 

The file structure for the program is as follows: 

```bash
└── src
├── car_park.py # Core car park management
├── display.py # Display device logic
├── sensor.py # Sensor device logic
├── main.py # Used to demonstrate functionality 
├── config.json # Sample .JSON config file
├── moondalup.txt # Sample log file 
└── tests/ 
├── test_car_park.py # Contains unit tests to verify CarPark functionality
├── test_display.py # Contains unit tests to verify Display functionality
└── test_sensor.py # Contains unit tests to verify Sensor functionality 
```


To use the system, navigate to src/main.py. Here, we can enter prompts to demonstrate the systems functionality.
main.py contains the following: 

```bash
#Import modules 
from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

# Initialise the car park
car_park = CarPark("Moondalup", 100, log_file="moondalup.txt")

#initialise the sensors and display 
entry_sensor = EntrySensor(1, car_park, True)

exit_sensor = ExitSensor(2, car_park, True)

display = Display(1, car_park, "Welcome to Moondalup", True)

# Simulate traffic
print("Cars entering:")
for i in range (10):
    entry_sensor.detect_vehicle()

print("\nCars exiting")
for i in range(2):
    exit_sensor.detect_vehicle()


# Write config to .JSON
car_park.write_config("moondalup_config.json")

# Load config from .JSON
car_park = CarPark.from_config("moondalup_config.json")
```
The src folder contains the log file "moondalup.txt" as well as config file "moondalup_config.json".
These files are here for demonstration purposes only, and can be deleted if desired. 