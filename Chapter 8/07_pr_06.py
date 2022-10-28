def rem_strip(string,word):
    newstr = string.replace(word,"")
    return newstr.strip()


a = input("Enter the string you want to strip: ")
b = input("Enter the word you want to remove: ")
print(rem_strip(a,b))


