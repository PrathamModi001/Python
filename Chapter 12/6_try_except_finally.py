try:
    n = int(input("Enter the number: "))
    if n<6:
        print("The number is smaller than 6!")
    else:
        print("The number is larger than 6!")

except Exception as e:
    print("Exception Encountered!")
    print(e)
    exit()

# So the order is: 
# sabse pehle try run hoga, if exception occured wo code run hoga.
# then IRRESPECTIVE of whatever that is written inside Exception (exit() hi kyu na likha ho), finally will ALWAYS run.
# difference btw normal line of code and code under finally is that when we write exit() in Exception then the normal line of code will not run. But the code inside finally will still run
finally:
    print("Ore wa Monkey D. Luffy, Kaizoku ou ni naru otoko da!")

print("Thanks for running the program!") # This will not be shown if there are any exceptions occuring in the code