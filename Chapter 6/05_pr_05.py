names = ["harry" , "kalash" , "preet" , "hrishi" , "ravi" , "modi"]

name = input("Enter the name to be checked in the database: ")

if name in names:
    print("You are allowed entry! Welcome!")
else:
    print("Sorry, You don't have access!")