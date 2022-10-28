from ast import Num


class Number:
    def sum(self):
        return self.a + self.b

num = Number() # Object Instantiation only after this the class will start taking memory
num.a = 12
num.b = 24

print(f"The sum of the two numbers is: {num.sum()}")