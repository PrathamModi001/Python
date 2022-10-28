class Library:
    def __init__(self):
        print("Books Present In The Libraray are: ")
        b = ["Algorithms" , "Django" , "Clrs" , "Python Notes"]
        books = "\n".join(b)
        print(books)
    
    def requestBooks(self,book1):
        self.book1 = book1
        Library.booksPresent.b.remove(self.book1)



lib = Library()
run = True
while run == True:
    print('''\n\n====== Welcome To The Central Library ======
        Please Choose an option:
        1. List of all the books
        2. Request a book
        3. Return/Donate a book
        4. Exit the library''')
    n = int(input("Enter a choice: "))
    
    if n == 4:
        exit()
    
    if n == 1:
        pass
        # lib.booksPresent()
    
    if n == 2:
        try:
            book = input("Enter the book you want to Issue: ")
            lib.requestBooks(book)
        except:
            pass