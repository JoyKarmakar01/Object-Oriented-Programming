class Distance:
    def __init__(self,x,y):
        self.feet = x
        self.inches = y
    def __add__(self,other):
        final_feet = self.feet + other.feet
        final_inches = self.inches + other.inches
        return Distance(final_feet, final_inches)
    def __str__(self):
        return "Distance : " + str(self.feet) + " feet and "+str(self.inches) + " inches" 

d1 = Distance(5,8)
d2 = Distance(4,10)
d3 = d1+d2
print(d3)