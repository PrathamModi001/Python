class Library:
    def __init__(self,books):
        self.books = books
    
    def display(self):
        sentence = "\n".join(self.books)
        print(sentence)
    
    def borrowBookAvailable(self,bookName):
        self.bookName = bookName
        if bookName in self.books:
            print(f"You have been issued {self.bookName}. Please keep it safe and return it within 30 days.")
            self.books.remove(self.bookName)
        else:
            print("Sorry the book isn't available at the moment.")
    
    def returnBook(self,bookName):
        self.bookName = bookName
        self.books.append(bookName)
        print("Task Completed!")

def exitMessage():
    print("Thanks for using this Library Management system!")


if __name__ == "__main__":
    lib = Library(["Algorithms" , "Django" , "Clrs" , "Python Notes"])
    run = True
    while run == True:
        print('''\n\n====== Welcome To The Central Library ======
            Please Choose an option:
            1. List of all the books
            2. Request a book
            3. Return/Donate a book
            4. Exit the library''')
        n = int(input("Enter a choice: "))
        
        try:
            if n == 4:
                exitMessage()
                exit()
            
            elif n == 1:
                lib.display()
            
            elif n == 2:
                name = input("Enter the book you want to issue: ")
                lib.borrowBookAvailable(name)
            
            elif n == 3:
                book1 = input("Enter the name of the book you want to return/donate: ")
                lib.returnBook(book1)
            
            else:
                print("Please enter a number between 1 and 4!")
        except Exception as e:
            print("Please enter valid inputs!")

exitMessage()