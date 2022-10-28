def greater_than_5(num):
    if num>5:
        return True
    else:
        return False

l1 = [1,2,3,4,5,6,7,8,9,10]
b = filter(greater_than_5,l1)
print(type(b))
print(list(b))

# SYNTAX: 
# b = filter({lamda or normal function} , {inputted list or list to work on})
# print(list(b)) because it will return a filter file which needs to be type casted into list