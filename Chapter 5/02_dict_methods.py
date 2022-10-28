myDict = {
    "Fast" : "As quick As A Fox",
    "Modi" : "Coder",
    "AnotherDict" : {"Lol" : "Lmao"},
    "Marks" : [1,2,5]
}

print(list(myDict.items()))
print("\n\n")
print(myDict.values())
print("\n\n")
print(myDict.keys())
print("\n\n")
myDict.update({
    "Dhapa" : "Friend",
    "Odu" : "Lodu"
})
print(myDict)

print("\n\n")
print(myDict["Dhapa"]) #This will return the value associated with the key "Dhapa"
print(myDict.get("Dhapa")) #This will return the value associated with the key "Dhapa"

#Difference between .get() and [] syntax:

print(myDict["Dhapa1"]) #Will return an ERROR
print(myDict.get("Dhapa1")) # Will return NONE not an error