import random

a = random.randint(0,100) # Random number generator between 0-100
print(a)

print("\n\n\nSnake(s) Water(w) Gun(g)")
print("==============================================\n\n")

b = input(f"Player 1: Your Turn: ") # Taking Input from user:

#  Assigning Computer snake water gun on random: 
if a<=33:
    c = "s"
elif a>33 and a<=66:
    c = "w"
else:
    c = "g"

print(f"The Computer Chose: {c}\n\n")

if b == "s" and c == "w":
    print(f"Congrats! You Won!")
elif b == "s" and c == "g":
    print(f"Oof! You Lost, Better Luck Next Time!")
elif b == "s" and c == "s":
    print(f"Wow What a turn of events! It Is a TIE!")


if b == "w" and c == "w":
    print(f"Wow What a turn of events! It Is a TIE!")
elif b == "w" and c == "g":
    print(f"Congrats! You Won!")
elif b == "w" and c == "s":
    print(f"Oof! You Lost, Better Luck Next Time!")

if b == "g" and c == "w":
    print(f"Oof! You Lost, Better Luck Next Time!")
elif b == "g" and c == "g":
    print(f"Wow What a turn of events! It Is a TIE!")
elif b == "g" and c == "s":
    print(f"Congrats! You Won!")





