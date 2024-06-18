class Employee:
    def __init__(self) -> None:
        self.name = "Joy"
        self.salary = 100000
    def __str__(self):
        return "Name : "+self.name+  " and His Salary = "+str(self.salary)
    
Joy = Employee()
print(Joy)