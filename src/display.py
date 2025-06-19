class Display:
    """
    Display to show messages and car park information.

    Attributes:
        id (int): Unique display identifier number.
        car_park (CarPark): Car park display is registered to.
        message (str): Message displayed
        is_on (bool): On/Off status of display.
    """
    def __init__(self, id, car_park, message="", is_on=False):
        """
        Initialises the display.

        Arguments:
            id (int): Display identifier number/
            car_park (CarPark): Car park display is registered to.
            message (str, optional): Message displayed. Defaults to empty ""
            is_on (bool, optional): On/Off status of display. Default false.
        """
        self.id = id
        self.car_park = car_park
        self.message = message
        self.is_on = is_on

    def __str__(self):
        """
        Prints display information.

        Returns:
             str: "Display [id]: [message]."
        """
        return f"Display {self.id}: {self.message}."

    def update(self, data):
        """
        Updates content of display.

        Arguments:
             data (dict): Key-value pairs:
                'message' (str): Display message.
                'available_bays' (int): Empty parking spaces remaining.
                'temperature' (float): Car park ambient temperature.
        """
        for key, value in data.items():
            if key == "message":
                self.message = value
            print(f"{key}: {value}")