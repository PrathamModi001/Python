n = int(input("Enter the number to find its multiplication table in form of a list: "))

a = [f"The Multiplication of {n}X{item} is: {n*item}\n" for item in range(1,11)]
print(a)