class car:
    def __init__(self,a = 50):
        self.speed = a
    def Get_Speed(self):
        return self.speed
    def Set_Speed(self,a):
        self.speed = a;
ob = car()
ob.Set_Speed(120)
print("Car speed is : ", ob.Get_Speed())
