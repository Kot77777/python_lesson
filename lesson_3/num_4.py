class Car:
    def __init__(self, capacity, speed, number):
        self.capacity = int(capacity)  # Преобразуем в целое число
        self.speed = int(speed)          # Преобразуем в целое число
        self.number = str(number)        # Преобразуем в строку

    def __str__(self):
        return "<Car capacity:%d speed:%d number:%s>" % (self.capacity, self.speed, self.number)