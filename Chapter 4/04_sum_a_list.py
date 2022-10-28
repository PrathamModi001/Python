print("Enter the numbers in list: ")
a = int(input()); b = int(input()); c = int(input()); d = int(input()); e = int(input());

number = [a,b,c,d,e]
print("\n",number)

print("The sum of the number is the list is: ")
sum1  = number[0] + number[1] + number[2] + number[3] + number[4]
print(sum1)

print("\nUsing Methods: ")
print(sum(number))