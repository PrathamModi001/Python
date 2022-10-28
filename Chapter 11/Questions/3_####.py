class Employee():
    salary = 3200
    increment = 1.5
    
    @property
    def totalSalary(self):
        return self.salary*self.increment
    
    @totalSalary.setter
    def totalSalary(self,salaryAfterIncrement):
        self.increment = salaryAfterIncrement/self.salary

harry = Employee()
print(harry.totalSalary)
harry.totalSalary = 4000
print(harry.increment)
        