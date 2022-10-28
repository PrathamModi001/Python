n = int(input("Enter the number to be checked: "))

prime=1
for i in range(2,n):
    if n%i==0:
        prime=0

if prime==1 and n!=2:
    print("The number entered IS a prime!")
else:
    print("NOT a prime!")