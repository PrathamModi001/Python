myDict = {}

for i in range(2):
    name = input("Enter the name of the student: ")
    number = int(input("Enter the Admission Number of the student: "))
    myDict.append({number:name})
    #myDict[number] = name
    


print(myDict)