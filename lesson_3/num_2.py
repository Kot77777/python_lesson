class Car:
    def __init__(self, capacity, speed, number):
        self.capacity = capacity
        self.speed = speed
        self.number = number

class RaceCar(Car):
    def __init__(self, speed, capacity=0, number=None):
        super().__init__(capacity, speed, number)
