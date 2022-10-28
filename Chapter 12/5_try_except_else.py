try:
    n = int(input("Enter the number: "))
    if n<6:
        print("The number is smaller than 6!")
    else:
        print("The number is larger than 6!")

except Exception as e:
    print("Exception Encountered!")
    print(e)

# So it is more like try except-else ladder. first try executes then if any exception encountered then the code shifts to the except part. 
# BUT if there are no exceptions then after try block of code the next executed will be else.
# So either except or else will be run not both.
else:
    print("No exceptions encountered! Mission Successful!")