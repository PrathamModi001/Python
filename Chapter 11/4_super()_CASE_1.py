class Person:
    country = "India"
    def takeBreath (self):
        print("I am breathing...") 
    
class Employee (Person):
    company = "Honda"
    def getSalary(self):
        print (f"Salary is {self.salary}")
    def takeBreath (self):
        print("I am an Employee so I am luckily breathing..")

class Programmer (Employee):
    company = "Fiverr"
    def getSalary(self):
        print (f"No salary to programmers")
        
        
    def takeBreath (self):
        print("I am a Programmer so I am breathing++..")
        super().takeBreath()
        # What super() does is that if there are multiple methods in parent child child classes and we want more tha one of those methods to be printed we use super(){repeated method} or {constructor}->{__init__}
        # Take a note: It is also used to take info from parent constructor like mentioned in above point
        # first take breath of programmer will run then for super() part it will take takBreath from the upar wala parent and also run that command 
        
p = Person ()
p.takeBreath()

e = Employee()
e.takeBreath()

pr = Programmer ()
pr.takeBreath() 