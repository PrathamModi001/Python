count = 0 # initialization
data = True # Forward Declaration types if you define it like data = "" it wont work!
with open("log.txt") as f:
    while data: # Jab tak data true evaluate ho rha hai (Matlab last line tak check hote jaega)
        data = f.readline() # isse ek ek line check hogi. count += 1 jab jab next line check hogi aisa logic
        count+=1
        if 'python' in data:
            print(f"'python' is present in {count}")