# Implement a student library system using oops where students can borrow a book from the list of books. Create a separate library and student class. Your program must be menu driven. You are free to choose methods and attributes of your choice to implement this functionality.

class Library():

    def __init__(self, listOfBooks):
        self.books=listOfBooks

    def displayAvailableBooks(self):
        print("\nAvailable books are:")
        for index, book in enumerate(self.books):
            if index!=0:
                print("\t\t\t",index,book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued '{bookName}'. Please keep it safe and return within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry! This book has been either issued to someone else or not available here right now. Please wait until the book will be returned or available. ")
            return False
    
    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book. Hope, you enjoyed reading it. ")

class Student():

    def requestBook(self):
        self.book=input("Enter the name of the book you want to borrow: ")
        return self.book
        
    def returnBook(self):
        self.book=input("Enter the name of the book you want to return: ")
        return self.book
        

    
if __name__ == '__main__':
    centralLibrary=Library(["","The Psychology Of Money", "Think and Grow Rich", "The Quick And Easy Way To Effective Speaking", "The Subtle Art Of Not Giving A F*ck", "Rich Dad And Poor Dad", "Think Like A Monk", "Ikigai"])

    student=Student()



    while True:
        welcomeMsg='''\n ================== Welcome to Central Library ==================

                    Please choose an option:
                    1. Listing all the books
                    2. Request a book
                    3. Add/Return a book
                    4. Exit the library
        '''
        print(welcomeMsg)

        a= int(input("Enter your choice: "))
        

        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for using Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid choice!")


