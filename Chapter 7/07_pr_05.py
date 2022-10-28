n = int(input("Enter the Nth number: "))

sum=0
i=0
while i<n:
    sum+=i
    i+=1
print(f"\nThe sum of the numbers till {n}th term is: {sum}")