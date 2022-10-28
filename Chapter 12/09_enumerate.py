import enum


list = [69,420,False,"Modi"]

# index = 0
# for item in list:
#     print(item,index)
#     index += 1

for index,item in enumerate(list): # Remember the ordser of index and item here. It is fixed!
    print(index,": ",item)