class Library:

    def __init__(self,ListOfBooks):
        self.availableBooks = ListOfBooks
    def displayAvailableBooks(self):
        print()
        print("available books:")
        for book in self.availableBooks:
            print(book)
        print()
    def LendBook(self,requestedBook):
        print()
        if requestedBook in self.availableBooks:
            print("you have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("sorry,the book is not available")
        print()
    def addBook(self,returnedBook):
        print()
        self.availableBooks.append(returnedBook)
        print("you have returned book,thanks")
        print()

class Customer:
    def requestBook(self):
        print()
        print("enter the name of book which you would like to borrow")
        self.book = input()
        print()
        return self.book
        
    def returnBook(self):
        print()
        print("enter the name of the book which you are returning")
        self.book = input()
        print()
        return self.book
        
        
        

library = Library(['book one','book two','book three'])
customer = Customer() 
while True:   
    print("1 display")
    print("2 request for the book")
    print("3 return book")
    print("4 to exit")
    userChoice = int(input())
    if userChoice is 1:
        library.displayAvailableBooks()
    elif userChoice is 2:
        requestedBook = customer.requestBook()
        library.LendBook(requestedBook)
    elif userChoice is 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice is 4:
        quit()
    else:
        print("operation isn`t available")
        