
def rec_sum(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return n + rec_sum(n-1)
    
n = int(input("Enter the Nth term to find its sum: "))
print(rec_sum(n))