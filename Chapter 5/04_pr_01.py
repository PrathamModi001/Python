from distutils.archive_util import make_tarball


matlab = {
    "Namaste" : "Hello",
    "Suprabhat" : "Good Morning",
    "Pankha" : "Fan",
    "Dabba" : "Box"
}

print("The translations of the following words is available: ")
matlab["All"] = "23"
print(list(matlab.keys()))

a = input("\n\n\nEnter the word to be translated: ")
print("\nThe meaning of the word entered is: ")
print(matlab.get(a))
