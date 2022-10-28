class Employee:
    Company = "Visa"
    
class Freelancer:
    Company = "Fiverr"
    level = 0
    
    def upgradeLevel(self):
        self.level = self.level + 1

# Parent Classes are Employee and Freelancer and both their features and objects are inherited to derived class: Programmer
class Programmer(Employee,Freelancer):
    name = "Rohit"
    
p = Programmer()
p.upgradeLevel()
# Even though we added the function upgradeLevel() in Freelancer class bt since it was inherited to class Programmer we can use this function through Programmer class 

print(p.Company) # What do you think will happen if we print this since both Employee() and Freelancer() have the Company Atrribute ?!
# Check the order of inheritance ! 
# since Employee inherited first: Programmer(Employee,Freelancer), So the Company of Employee will take precedence
# But if the derived class has its own Company Attribute then it will be shown as the company of employee will be overwritten (as dicussed earlier)
print(p.level)