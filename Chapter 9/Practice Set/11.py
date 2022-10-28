# import os

# os.rename('lol.txt', 'renamed_by_python.txt')

with open("lol.txt") as f:
    old = f.read()
import os
os.remove("lol.txt")

with open("renamed_by_python.txt" ,"w") as f:
    f.write(old)