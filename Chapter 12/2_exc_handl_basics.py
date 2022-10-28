while(True):
    print("Press 'q' to quit the game.\n")
    n = input("Enter the number: ")
    
    if n == 'q':
        break
    # if n != q fir ye code TRY karo. agar n integer hoga to to ye code run ho jaega. Agar character hoga to fir sirf TRY karo run karne ka
    # Agar user enters some character to niche ka code dekho, then wo pehle TRY karega to run the code so pehli line: Trying... print hoga whether or not char hai ya integer suggesting char ho ya int compiler iss piece of code ko run karne ki puri puri TRY kar rha hai
    # jab bhi koi error waali line of code aa jaega tab move to except wala piece of code.
    # fir except waale code mein dikha do user ko kya error/ mistake hai.
    try:
        print("Trying...")
        n = int(n)
        if n<6:
            print("The number entered is samller than 6!")
        else:
            print("The number entered is larger than 6!")
    except Exception as e:
        print(e)
        print("Please enter an integer!")
        

print("Thanks for playing the game with me!")