class Company:
    def __init__(self,name,salary,subunit):
        self.name = name; self.salary = salary; self.subunit = subunit
        print("The constructor class is called for Company!\n\n")
    
    def getDetails(self):
        print(f"The name of the employee is {self.name}. The respective salary of the employee is {self.salary}.\nThe subunits where the employee is going to overwatch are {self.subunit}")

pratham = Company("Pratham" , 100, "YouTube")
pratham.getDetails()