class Animals:
    @staticmethod
    def eat():
        print("animal is eating")
class Pets(Animals):
    @staticmethod
    def petting():
        print("owner is petting the pet")
class Dog(Pets):
    def __init__(self,name):
        self.name = name
    def bark(self):
        print(f"{self.name} is barking")