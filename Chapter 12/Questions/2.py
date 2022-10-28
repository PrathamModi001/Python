list1 = [11,22,33,44,55,66,77,88,99,100]

for index,item in enumerate(list1):
    if index%2!=0 and index!=1 and index<=7:
        print(item,index)