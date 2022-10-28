from audioop import mul


# Check the place where we put the str tag
# Since we are to have the output as 7*i so putting that as the string is the most apporpriate

list1 = [str(7*i) for i in range(1,11) ]

mult_table = "\n".join((list1))
print(mult_table)