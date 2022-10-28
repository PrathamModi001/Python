from mimetypes import init


n = int(input("Enter the number to find its reciprocal: "))

try:
    c = 1/n
    print(c)
    
except ZeroDivisionError as e:
    print("Infinity.")
    
except:
    print("Invalid Input!")