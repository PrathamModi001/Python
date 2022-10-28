from random import gauss


class Employee:
    comany = "Bharat Gas"
    salary = 5600
    salaryBonus = 500
    
    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus
    
    # what we want is changing/variable salary bonus. if salary is given and total salary is given and we want to find the salaryBonus we can use this type of decorator
    
    @totalSalary.setter
    def totalSalary(self,totalSal):
        self.salaryBonus = totalSal - self.salary

harry = Employee()
harry.totalSalary = 6000
print(harry.salary)
print(harry.salaryBonus)