with open("this.txt") as f:
    data = f.read()

with open("this_copy.txt" , "w") as f:
    f.write(data)