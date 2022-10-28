with open("this.txt") as f1:
    data1 = f1.read()
with open("this_copy.txt") as f2:
    data2 = f2.read()

if data1 == data2:
    print("The files are identical!")
else:
    print("The files are not identical!")