import math
class Calculator:
    def squared(self,x):
        self.x = x
        return x**2
    def cubed(self,x):
        self.x = x
        return x**3
    def sqroot(self,x):
        self.x = x
        return math.sqrt(x)
    
    @staticmethod
    def greet():
        print("Done with the calculations!")

print("Simple Calculator Using Classes\n")
print("========================================================================\n")
print('''The calculator has the following functions: 
      's' -> Square
      'c' -> Cubed
      'r' -> SquareRoot\n\n''')
n = int(input("Enter the number: "))
calc = Calculator()
a = input("Enter the operations to be done on the number from the list provided above: ")

if a == 's':
    print(f"The Square of the number {n} is {calc.squared(n)}!")
        
if a == 'c':
    print(f"The Cube of the number {n} is {calc.cubed(n)}!")
        
if a == 'r':
    print(f"The Square Root of the number {n} is {calc.sqroot(n)}!")
        
else:
    print("Invalid Response!")

calc.greet()