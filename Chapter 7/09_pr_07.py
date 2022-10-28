n = int(input("Enter the number of rows in the pattern: "))

for rows in range(n):
    print(" " * (n-rows-1), end = "")
    print("*" * (2*rows+1), end = "")
    print(" " * (n-rows-1))

