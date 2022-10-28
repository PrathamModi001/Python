#  It is the older form of fstring

name = "Harry"
channel = "CodeWithHarry"
type = "Coding"
# a = f"This is {name}"
# a = "This is {}".format(name)

# Multiple Format()
# a = "This is {} and his channel is {}".format(name, channel)

# Indexing the {} to choose where to put which variable. so the first name will go in 0 next in 1 and so on...
# a = "This is {0} and his {2} channel is {1}".format(name, channel, type)


a = "This is {} and his {} channel is {}".format(name, channel, type)
print(a)