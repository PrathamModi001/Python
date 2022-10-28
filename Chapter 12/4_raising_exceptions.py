try:
    def Increment(a):
        return a+1
except:
    raise ValueError("This is not good - Modi") # custom messages to show when this error occurs here.
    # It just means that when the function's input 'a' is not proper it should give out value error exception irrespective of the actual error and we can print the custom message later.