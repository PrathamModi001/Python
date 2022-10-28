maths = int(input("Enter your marks in Maths: "))
phy = int(input("Enter your marks in Physics: "))
chem = int(input("Enter your marks in Chemistry: "))

if(maths>=33 and phy>=33 and chem>=33):
    if((maths + phy + chem)>=160):
        print("\n\nYou have successfully PASSED the exam! Congrats!")
    else:
        print("\n\nYou have FAILED the exam! Better luck next time!")

else:
    print("\n\nYou have FAILED the exam! Better luck next time!")