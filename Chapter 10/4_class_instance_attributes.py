class Company:
    company = "Google"
    salary = 100 # Creating class attributes (like default value of salary until defined again(inst attribute))

harry = Company()
rajni = Company()

# Creating instance attributes
# If intance attribute present, it will take priority over class attributes
harry.salary = 300
rajni.salary = 400