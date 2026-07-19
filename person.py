class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def displayinfo(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")