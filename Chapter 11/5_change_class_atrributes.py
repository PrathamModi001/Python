# *************** __ walle methods ko dunder('D'ouble 'UNDER'score) or magic methods bhi bolte hai************************



class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"
    
    def changeSalary(self, sal):
        self.salary = sal # this will always change the instance attributes only and n ot the class attributes
        
    
    # 1st Way
    # def changeClassSalary(self,sall):
        # this will chnage the class attributes also!
        # self.salary = sall
        # self.__class__.salary 
    
    #2nd Way  
    @classmethod # this is called a decorator
    def changeClassSalary(cls,sall):
        cls.salary = sall
    # By doing this we can change the class attributes and also 
    # ADD CLASS ATTRIBUTES!
        
e = Employee()
print(e.salary)
e.changeSalary (455) # Will change the instance attribute and not the class attribute
print(e.salary) # printing the instance attribute
print("\n\nNow employing the class attribute changing function")
e.changeClassSalary(455)
print (Employee.salary)