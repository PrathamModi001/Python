n = int(input("Enter the number to print its multiplication table: "))

# For Loop
# for i in range(1,11):
#     print(str(n) + " X " + str(i) + " = " + str(i*n))


# While Loop
i=1
while i<=10:
    # print(str(n) + " X " + str(i) + " = " + str(i*n))
    print(f"{n} X {i} = {i*n}") # Using F string
    i+=1