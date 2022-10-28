def cel_to_far(x):
    f = (x * (9/5) + 32)
    return f


n = int(input("Enter the temperature in degree CELSIUS: "))
print(f"\n\nThe converted temperature in degree FAHRENHEIT is: {cel_to_far(n)}")

