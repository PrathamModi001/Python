with open("log.txt") as f:
    data = f.read()

if 'python' in data:
    print("Yes, 'python' is presnt in the log file!")
else:
    print("Sorry, 'python' is not present in the log file!")