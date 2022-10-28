def game():
    return 69

n = int(input("Enter the score: "))
m = game()

if n>m:
    f = open("HiScore.txt", "w")
    data = f.write(f"Congrats! You just scored the highest: {n}")
    f.close()
else:
    f = open("HiScore.txt", "w")
    data = f.write(f"Sorry! The highest score is still {m}.\nBetter Luck Next Time!")
    f.close()

print("The results have come! Please check the text file!")