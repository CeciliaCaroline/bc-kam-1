class Car:
    num_of_doors = 4
    num_of_wheels = 4
    speed = 0

    def __init__(self, name='General', model='GM', car_type=None):
        self.name = name
        self.model = model
        self.car_type = car_type
        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2
        if self.car_type == 'trailer':
            self.num_of_wheels = 8

    def is_saloon(self):
        if self.car_type == 'trailer':
            return False
        else:
            return True

    def drive(self, speed):
        if self.is_saloon():
            self.speed = speed * (1000/3)
        else:
            self.speed = speed * 11
        return self
