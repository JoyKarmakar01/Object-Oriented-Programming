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
ob = car()

print("Car speed is : ", ob.Get_Speed())
ob.Set_Speed(800)
print("New Car Speed is : ", ob.Get_Speed())
ob.Set_Speed(90)
print("New car speed : ",ob.Get_Speed())

