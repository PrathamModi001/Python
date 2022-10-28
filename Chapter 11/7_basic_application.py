class Complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __add__(self,other):
        return self.a + other.a , self.b + other.b

n1 = Complex(6,9)
n2 = Complex(3,5)
n3 = n1 + n2
print(n3)