def factorial_iterative(a):
    fact = 1
    for i in range (1,a+1):
        fact *= i
    return fact

def factorial_recursive(b):
    if b == 1 or b == 0:
        return 1
    return factorial_recursive(b-1) * b


n = int(input("Enter the number to find its factorial: "))
# print(factorial_iterative(n))

print("The recursive method: ")
print(factorial_recursive(n))

