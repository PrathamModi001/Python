class Complex():
    def __init__(self,x,y):
        self.x = x; self.y = y;
    def __str__(self):
            return f"The Complex Number given is: {self.x} + {self.y}i\n"
    
    def __add__(self,other):
        return f"The sum of the two complex numbers is: ({self.x + other.x} , {self.y + other.y}i)"
    
    def __mul__(self,other):
        return f"The multiplication of the two complex numbers is: ({self.x*other.x - self.y*other.y} , {self.x*other.y + self.y*other.x}i)"

c1 = Complex(3,2)
print(c1)
c2 = Complex(1,7)
print(c2)
print(c1+c2)
print(c1*c2)


