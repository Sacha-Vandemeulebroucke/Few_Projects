from books import books

class Book:

    library = []

    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def the_book(self):
        return {"title" : self.title,"author": self.author, "year": self.year}

    def add_to_the_library(self):
        Book.library.append(Book.the_book(self))

    @staticmethod
    def remove_from_library(title):
        for i, book1 in enumerate(Book.library):
            if book1['title'] == title:
                Book.library.remove(Book.library[i])
        print(f"The book {title} has been removed successfuly from the library")

    @staticmethod
    def search_in_library(title):
        for i, book1 in enumerate(Book.library):
            if book1['title'] == title:
                print(f"Book found : {Book.library[i]['title']} by {Book.library[i]['author']} written in {Book.library[i]['year']}")
                break
            elif i == len(Book.library)-1 and book1['title'] not in Book.library:
                print(f"The book {title} was not found")

    @classmethod
    def print_library(cls):
        print(cls.library)

    @classmethod
    def print_library_title(cls):
        for book in cls.library:
            print(book['title'])



for book in books:
    Book(book[0], book[1], book[2]).add_to_the_library()



Book.print_library()
print()
Book.print_library_title()
print()
Book.remove_from_library("To Kill a Mockingbird")
print()
Book.print_library_title()
print()
Book.search_in_library("The Lord of the Rings")
print()
Book.remove_from_library("Don Quixote")
print()
Book.search_in_library("Don Quixote")