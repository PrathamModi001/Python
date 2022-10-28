class Person:
    country = "India"
    def takeBreath (self):
        print("I am breathing...")
        
    def __init__(self): # Normal sa constructor
        print("Initializing Person...")
    
class Employee (Person):
    company = "Honda"
    def getSalary(self):
        print (f"Salary is {self.salary}")
        
    def takeBreath (self):
        super().takeBreath()
        print("I am an Employee so I am luckily breathing..")
        
    def __init__(self):
        super().__init__() #super().__init__() is used to call the constructor from the pichhle parent ka constructor
        print("Initialising Employee...")

class Programmer (Employee):
    company = "Fiverr"
    def getSalary(self):
        print (f"No salary to programmers")
        
    def takeBreath (self):
        super().takeBreath()
        print("I am a Programmer so I am breathing++..")
        
    def __init__(self):
        super().__init__()# this calls the constructor from its parent class which contains the constructor to its parent class and so in the end it starts to contain all the initialising: Person Employee Programmer
        print("Initialising Programmer...")
        
p = Person ()
p.takeBreath()

e = Employee()
e.takeBreath()

pr = Programmer ()
pr.takeBreath() 