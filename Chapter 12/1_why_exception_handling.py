n = int(input("Enter the number: "))

if n<6:
    print("The number is smaller than 6!")
else:
    print("The number is greater than 6!")

# So now the question is,
# What if the user doesnt enter an integer (which we are typecasting a string->integer as input() only takes strings) but the characters CANT be typecasted to int
# So we are thrown a 'value error' which crashes our program which we absolutely dont want. we want the error to be shown to the user and not crash the entire program.
# So that is why we have the concept of exception handling.


