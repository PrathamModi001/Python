from functools import reduce
l1 = [99,1234,123,11,12,435,8867]

max_self = lambda a,b:max(a,b)

val = reduce(max_self,l1)
print(int(val))
