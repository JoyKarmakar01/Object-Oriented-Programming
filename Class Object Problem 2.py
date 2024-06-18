class person:
    def __init__(self, name, gender):

        self.Name = name
        self.Gender = gender

    def ShowInfo(self):
        print("Name : ", self.Name)
        print(f"Gender : {self.Gender}")
        
    
p1 = person("John Doe", "Male")
p2 = person("Jane Smith", "Female")

print("Person 1 Information:\n")
p1.ShowInfo()
print("\nPerson 2 Information:")
p2.ShowInfo()
