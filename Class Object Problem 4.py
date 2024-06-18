class car:
    def __init__(self,a = 50):
        self.Set_Speed (a)
    def Get_Speed(self):
        return self._speed
    def Set_Speed(self,a):
        if a<= 0 or a>= 160:
            print("Speed needs to be 0-160")
        else:
            self._speed = a;
    speed = property(Get_Speed,Set_Speed)
ob = car(100)
print(ob.speed)
ob.speed=200
print(ob.speed)
ob.speed=80
print(ob.speed)


