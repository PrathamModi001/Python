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
        
p = Person ()
p.takeBreath()

e = Employee()
e.takeBreath()

pr = Programmer ()
pr.takeBreath() # Again the same q, takeBreath() will take from which class Employee or Person ?
# Note that: the heirarchy is: Person->Employee->Programmer
# Ans: person se employee mein takeBreath() inh. Employee mein khud ka takeBreath() so wo overwritten. Programmer inh Employee. So employee ka takeBreath() show karega
# So The latest inheritance will give us the answer of the Method.
# Using this concept: If programmer would have its own takeBreath() it would be the Method shown

print(pr.country)
# since programmer ke paas nahi, Employee ke paas nahi only Person ke paas country method hai to sirf wahi show hjoga nd nothing else kyuki no other option of inheritance