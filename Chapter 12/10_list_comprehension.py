a = [1,2,44,523,58,347,34,886,74,33,69,13]

# b = []
# for item in a:
#     if item%2 == 0:
#         b.append(item)

# print(b)

# Shortcut to write the same code:
b = [item for item in a if item%2==0]
print(b)