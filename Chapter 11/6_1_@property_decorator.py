from random import gauss


class Employee:
    comany = "Bharat Gas"
    salary = 5600
    salaryBonus = 500
    
    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus

harry = Employee()
print(harry.totalSalary) # see this is a property and not a function
# a function would be harry.totalSalary().
# So @property returns everything as a property
# This is also called getter method
    