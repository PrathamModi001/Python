def greet(name):
    print(f"Good Morning, {name}")
# Just assume this as a massive piece of code which is also needed in the next file but copying is not efficient.
# Note that we ONLY want this function to be passed on to the next file. NOT the next part of code i.e. Enter the name and all that
# =======================================================================

#if you run this code in the current file it will show : '__main__'
print(__name__)
# but if you run this code in other file (by importing) it will show the name of this file i.e.'m07_file1.py

# so this print is used to check whether the module is running from the file or is it imported
# =======================================================================
# what we want is that only the piece of code below should run if run from only this file and not from next file
# so we write this:
if __name__ == "__main__":
# iss line ka matlab hai ki same file run ho rhi hai ya nahi
    
    n = input("Enter the name of the user: ")
    greet(n)