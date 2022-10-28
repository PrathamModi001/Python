class Employee(): #Making a normal class
    company = "Google" # default value of 'company' set
    
    def showCompany(self):
        print(f"The company you are working for is {self.company}")
    
    def showDetails(self):
        print("This is an employee")

# This is how you use inheritance
# Employee is now inherited to Programmer.
# All the features of the class employee are now available to pragrammer
# Employee -> Base Class. Programmer -> Derived Class
class Programmer(Employee):
    language = "Python"
    
    def getLanguage(self):
        print(f"The language that you are working on is: {self.language}")
    
    def showDetails(self):
        print("This is a programmer")
    # Since all the features are inherited now there are two showDetails(). Which will the code follow?
    # ALWAYS the function in derived class wil be run as the function present in base class gets overidden (latest value dikhayenge in short)
    # So since there is a showDetails() present in baseclass but the showDeatils in derived class will be shown!

e = Employee()
p = Programmer()
e.showCompany()
e.showDetails()
print("\n\n")
p.getLanguage()
p.showCompany()
p.showDetails()    
    