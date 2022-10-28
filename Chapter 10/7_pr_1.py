class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,language,position):
        self.name = name; self.salary = salary; self.language = language; self.position = position
    
    def getInfo(self):
        print(f"Hello Mr/Mrs. {self.name},\nThe language you are the most familiar with is {self.language}.\nThe position for which you applied was {self.position} and the respective salary that you are asking for is {self.salary}.\n\n")

harry = Programmer("Harry",100000,"Python","Lead Developer")
harry.getInfo()