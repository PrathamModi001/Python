f = open("poems.txt")
data = f.read()

if 'Twinkle' in data:
    print(f"The Word 'Twinkle' is present!")
else:
    print("The Word 'Twinkle' is NOT present!")