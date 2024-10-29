class GasStation:
    def __init__(self, C):
        self.C = C
        self.fillfull = 0

    def fill(self, n):
        if (self.fillfull + n) <= self.C:
            self.fillfull += n
        else:
            raise Exception

    def tank(self, n):
        if(self.fillfull) > n:
            self.fillfull -= n
        else:
            raise Exception

    def get_limit(self):
        return (self.fillfull)

s = GasStation(1000)
s.fill(300)
print(s.get_limit())
s.tank(100)
s.fill(300)
print(s.get_limit())
for i in range(5):
    s.tank(50)
print(s.get_limit())
s.fill(1000)
for i in range(50):
    s.tank(100)
print(s.get_limit())
