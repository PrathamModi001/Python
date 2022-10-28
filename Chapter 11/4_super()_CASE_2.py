class Person:
    country = "India"
    def takeBreath (self):
        print("I am breathing...") 
    
class Employee (Person):
    company = "Honda"
    def getSalary(self):
        print (f"Salary is {self.salary}")
        
    def takeBreath (self):
        # ye pura takeBreath() print karega (meaning ye dono chize print hongi)
        super().takeBreath() # isko print karne ke liye upar waale takeBreath() pe pohoch jayenge
        print("I am an Employee so I am luckily breathing..")

class Programmer (Employee):
    company = "Fiverr"
    def getSalary(self):
        print (f"No salary to programmers")
        
    def takeBreath (self):
        super().takeBreath() # ye le jayega upar waale takeBreath() pe
        # so the upar wala super() contains
        # 1. super()(programmer) -> super() (employee)(since take breath contains multiple lines iski wajah se niche wala 2 printed) -> takeBreath(person)
        # 2. printed because of super() (employee) i am an employee so i am luckily braething
        # 3.
        print("I am a Programmer so I am breathing++..")
        
p = Person ()
p.takeBreath()

e = Employee()
e.takeBreath()

pr = Programmer ()
pr.takeBreath() 