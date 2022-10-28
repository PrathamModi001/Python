def squared(num):
    return num*num

l1 = [1,2,3,4,5]

# Method 1:
# l2 = []
# for item in l1:
#     l2.append(squared(item))
    
# print(l2)

# Method 2:
# syntax: 
# b = map({lamda function} or {normal function} , {inputted list}))
# {required list} = list(b)

#  or {required list} = list(map({lamda function} or {normal function} , {inputted list}))
# you need to type cast it to list as it returns a map
b = map(squared,l1)
print(list(b))
# print(list(map(squared,l1))) also if you can actually read the code
