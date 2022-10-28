with open("abusive.txt") as f:
    raw = f.read()

if 'Madarchod' in raw:
    edit = raw.replace("Madarchod" , "#&%$!*@")
    with open("abusive.txt","w") as f:
        f.write(edit)

print("Work done please check the text file!")