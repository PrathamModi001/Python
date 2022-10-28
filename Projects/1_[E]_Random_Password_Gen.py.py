# Writing the random password generator with the sequence of the letters numbers and symbols also being random

import string
import random

alphabets = string.ascii_lowercase + string.ascii_uppercase # gets all the letters lowercase + uppercase
numbers = string.digits # gets all the digits
symbols = ["!","@","#","$","%","^","&","*","(",")","_","+"] # dont know how to get all symbols so manual work here
print("Welcome to the PyPassword Generator")
print("===========================================================\n\n")

alphabet = int(input("How many letters would you like in your password? \n"))
symbol = int(input("How many symbols would you like? \n"))
number = int(input("How many numbers would you like? \n"))

x = random.randint(1,100)
y = random.randint(1,100)
z = random.randint(1,100)

print("\nHere is your password: ")

# Number Symbol Letter
if x>y and x>z:
    for i in range(number):
        print(random.choice(numbers),end="")
    for i in range(symbol):
        print(random.choice(symbols),end="")
    for i in range(alphabet):
        print(random.choice(alphabets),end="")

# Letter Number Symbol
elif y>z:
    for i in range(alphabet):
        print(random.choice(alphabets),end="")
    for i in range(number):
        print(random.choice(numbers),end="")
    for i in range(symbol):
        print(random.choice(symbols),end="")

# Symbol Letter Number
else:
    for i in range(symbol):
        print(random.choice(symbols),end="")
    for i in range(alphabet):
        print(random.choice(alphabets),end="")
    for i in range(number):
        print(random.choice(numbers),end="")