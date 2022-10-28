import numbers


class Number():
    def __init__(self,num1):
        self.num1 = num1
    # when we want to use operators in userdefined data types (called classes) we must use dunder/magic methods and the following syntax: the operations include __add__ __mul__ 	__sub__ __truediv__ __floordiv__ __mod__ __pow__
    def __add__(self,num2):
        return self.num1 + num2.num1

n1 = Number(1)
n2 = Number(2)
print(n1+n2)

# full article on gfg:
# https://www.geeksforgeeks.org/operator-overloading-in-python/