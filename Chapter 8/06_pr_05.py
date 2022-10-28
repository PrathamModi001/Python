def pattern(n):
    i = n
    # while i>=0:
    #     print("*" * i)
    #     i-=1
    for i in range(n):
        print("*" * (n-i))
        
n = int(input("Enter the number of rows in the pattern: "))
pattern(n)