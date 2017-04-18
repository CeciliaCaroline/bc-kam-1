class Mobile:
    # This is the base class for a mobile phone
    # With a default screen size and battery
    screen_size = 4
    battery = 'lithium'

    def __init__(self, name, model, processor, internal_memory, imei):
        self.imei = imei
        self.internal_memory = internal_memory
        self.processor = processor
        self.model = model
        self.name = name

    def dail_number(self, number):
        return 'Calling ' + number

    def send_message(self, message):
        return 'sending message to one person : ' + message


class Samsung(Mobile):
    # Samsung mobile phone inherits from the Mobile class
    # Overiding the default screen size with a new screen size
    screen_size = 5

    # Samsung phone has a camera, and it can be started in a normal mode or panorama mode.
    # Normal mode if no mode specified
    def start_camera(self, mode=None):
        if mode is None:
            return 'starting camera '
        else:
            return 'starting camera in ' + mode + 'mode'

    # A samsung phone can send a message to a group of people.
    def send_message(self, message):
        return 'sending message to a group: ' + message


class Nokia(Mobile):
    # Nokia mobile phone uses a different battery
    battery = 'Li-on'

    # Nokia phone connects bluetooth devices differently
    def connect_bluetooth(self):
        return 'Pair with only nokia phones'
