def divThanFive(num):
    if num%5==0:
        return True
    else:
        return False

list1 = [1,2,3,6,5,10,13,15,64,6775,436,3427,4,510,1245]

b = filter(divThanFive,list1)
print(list(b))
