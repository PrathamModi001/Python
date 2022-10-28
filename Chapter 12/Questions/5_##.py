n = int(input("Enter the number to find its multiplication table in form of a list: "))

a = [n*item for item in range(1,11)]
print(a)

with open("Tables.txt" , "a") as f:
    f.write(str(a))
    f.write("\n\n")