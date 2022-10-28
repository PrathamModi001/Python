from functools import reduce
l1 = [1,2,3,4]

sum = lambda a,b:a+b

val = reduce(sum,l1)
print(val)

# it does sequential rolling
# 1,2 pe sum lambda funct applied jisse 3
#  3+3 -> 6... 6+4--> 10
#  so output is 10