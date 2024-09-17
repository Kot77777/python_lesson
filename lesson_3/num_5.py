class Car:
    def __init__(self, capacity, speed, number):
        self.capacity = capacity
        self.speed = speed
        self.number = number

    def __eq__(self, other):
        if isinstance(other, Car) == 1:
            return self.number == other.number
        else: return False

    def __hash__(self):
        return hash((self.number))