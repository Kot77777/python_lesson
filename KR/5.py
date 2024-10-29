class SpacePort:
    def __init__(self, size):
        if size > 0:
            self.size = size
            self.sp = [False] * size
        else:
            raise Exception

    def request_landing(self, dock_number):
        if dock_number >= self.size or dock_number < 0:
            raise Exception
        if self.sp[dock_number] == True:
            return False
        if self.sp[dock_number] == False:
            self.sp[dock_number] = True
            return True

    def request_takeoff(self, dock_number):
        if dock_number > self.size or dock_number < 0 or self.sp[dock_number] == False:
            raise Exception
        if self.sp[dock_number] == True:
            self.sp[dock_number] = False
            return True

s = SpacePort(5)
print(s.request_landing(0))
print(s.request_landing(4))
try:
    print(s.request_landing(5))
except:
    print("Ooops")

print(s.request_takeoff(0))
print(s.request_takeoff(4))
try:
    print(s.request_takeoff(5))
except:
    print("Ooops")