class Animals():
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def Bark():
        print("Bhow Bhow!")

a = Animals()
p = Pets()
d = Dog()
d.Bark()

# This is a multilevel Inheritance