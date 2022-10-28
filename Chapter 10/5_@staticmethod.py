class Employee:
    company = "Google"
    def getsalary(self,signature):
        print(f"Your current salary working as a Lead Management Commitee member at {self.company} is {self.salary}.\n{signature}")
    
    # when the function is not at all dependant on self(objects) use @staticmethod
    @staticmethod
    def greet():
        print(f"Waddup fam")

harry = Employee()
harry.salary = 3000000
harry.getsalary("With Regards,\nHarry") #Argument form you can also do harry.signature = with regards and remove the attribute in line 3 to only self. but since we have done extra attribute we wil specify signature in getsalary method only
harry.greet()