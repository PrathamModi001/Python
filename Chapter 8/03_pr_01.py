def great(a,b,c):
    if a>b and a>c:
        print(f"\n\n{a} is the greatest of the three numbers: ")
    elif b>c:
        print(f"\n\n{b} is the greatest of the three numbers: ")
    else:
        print(f"\n\n{c} is the greatest of the three numbers: ")

def maximum(num1,num2,num3):
    if (num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    
    else:    
        if(num2>num3):
            return num2
        else:
            return num3
    
print("Enter the three numbers: ")
a = input()
b = input()
c = input()

great(a,b,c)