class Number():
    def __init__(self,a):
        self.a = a
    
    
    # if we directly print an object like n = Number(69) and print(n)
    # the output will be: <__main__.Number object at 0x000002626E57E6A0>
    
    # which is absolutely not desirable 
    # so when we want something always printed immediately when an object is created we can use __str__ magic method
    def __str__(self):
        return f"The Number is: {self.a}"

n = Number(69)
print(n)