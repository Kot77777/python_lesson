class Garage:

    # Конструктор и деструктор, если нужны
    def __init__(self):
        self.sp = []

    # Запарковать машину v
    def park(self, v):
        self.sp.append(v)

    # Пересчитать машины заданного типа t.
    # Вернуть количество.
    def count(self, t):
        return sum([isinstance(i, t) for i in self.sp])

    # Получить самую быструю машину заданного типа t.
    # Вернуть экземпляр.
    def get_fastest_of_type(self, t):
        larg = 0
        for i in self.sp:
            if isinstance(i, t):
                if i.speed > larg:
                    k = i
                    larg = i.speed
        return k