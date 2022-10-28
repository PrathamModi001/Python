print("=======================================")
print("Welcome to THE PERFECT GUESS!\n")
print('''Instructions:
      -> Guess the secret number!
      -> If the guess is higher you'll be told to guess lower
      -> If the guess is lower you'll be told to guess higher
      -> Play the game and enjoy!\n''')
print("=======================================")
name = input("Enter the player name: ")
import random

a = random.randint(0,100)

# print(f"the secret number is: {a}")

flag = 0
count = 0
while flag == 0:
    n = int(input("Enter the number: "))
    count+=1
    
    if n == a:
        print(f"Congrats! You have guessed the number correctly.\nIt was {n} and you guessed it in {count} tries!")
        flag = 1
    
    else:
        if n > a:
            print("Too high! Guess Lower\n")
        else:
            print("Too low! Guess Higher\n")

with open("HiScore.txt", "r") as f:
    score = int(f.readline())

if(count<score):
    with open("HiScore.txt", "w") as f:
        f.write(str(count))
        f.write(f"\n{name} just broke the Record!")
    
print("\n\nThanks for playing this simple game with me 😁")