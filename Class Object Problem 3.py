class person:
    counter = 0
    def __init__(self, name, gender):

        self.name = name
        self.gender = gender
        person.counter  +=1

    def ShowInfo(self):
        print("Name : ", self.name)
        print(f"Gender : {self.gender}")
        
    @staticmethod    
    def ShowCount():
        print('Number of objects creater so far: ', person.counter)


p1 = person("John Doe", "Male")
p2 = person("Jane Smith", "Female")
person.ShowCount()

