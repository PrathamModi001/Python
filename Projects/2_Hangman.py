import random
word_list = ["ardvark" , "baboon" , "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for i in range(len(chosen_word)):
    display.append("_")

end_of_game = False
while not end_of_game:
    guess = input("Guess the letter ").lower()
    for i in range(len(chosen_word)): # checks by indexing method
        if chosen_word[i] == guess:
            display[i] = guess
        else:
            pass
    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("Congrats! You won!")


