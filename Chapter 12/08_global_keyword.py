a=54 #Global variable
def func1():
    global a # global a ko yaha bula liya
    print(f"Print statement 1: {a}")
    a=8 #Local Variable if global keyword is not used. so it will change the global variable itself
    print(f"Print statement 2: {a}")
    
func1()
print(f"Print statement 3: {a}")