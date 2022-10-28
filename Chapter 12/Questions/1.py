# try:
#     for i in range(1,4):
#         with open(f"{i}.txt") as f:
#             pass

# except Exception as e:
#     print("Please make sure the files are presnt in the subfolder!")
#     print("The Exception in technical terms: ")
#     print(e)

def readFIle(filename):
    try:
        with open(filename,"r") as f:
            print(f.read)
    except FileNotFoundError as e:
        print("Please make sure the files are presnt in the subfolder!")
        print("The Exception in technical terms: ")
        print(e,"\n")

for i in range(1,4):
    readFIle(f"{i}.txt")