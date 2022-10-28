a = int(input("Enter the marks of student number 1: "))
b = int(input("Enter the marks of student number 2: "))
c = int(input("Enter the marks of student number 3: "))
d = int(input("Enter the marks of student number 4: "))
e = int(input("Enter the marks of student number 5: "))
f = int(input("Enter the marks of student number 6: "))

marks = [a,b,c,d,e,f]
print("\n\nThe marks of the student UNSORTED: ")
print(marks);
print("==================================\n")
print("SORTED")
marks.sort()
print(marks)