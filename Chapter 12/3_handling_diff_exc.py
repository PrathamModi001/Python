from decimal import DivisionByZero


while(True):
    try:
        n = int(input("Enter the number to find its reciprocal: "))
        c = 1/n
        print(c)
        break
    
    # The value error will be handled by this code block
    except ValueError as e:
        print("Please Enter a valid value\n!")
    
    # The division by zero error will be handled by this code block    
    except ZeroDivisionError as e:
        print("Make sure the division is not with zero!\n")
    
    # Every other exception except the two mentioned will come under this category. it is more like if elif else ladder kinda thing where except: is like else.
    except:
        print("Invalid Input! Please re-read the instructions and enter accordingly.")

print("Thanks for using the code!")