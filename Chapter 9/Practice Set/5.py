with open("gaali.txt") as f:
    raw = f.read()

list = ["Laude", "Behenkelode","Chutiye","Gand", "Behenchod"]

for word in list:
    raw = raw.replace(word,"_____")
    with open("gaali.txt","w") as f:
        f.write(raw)