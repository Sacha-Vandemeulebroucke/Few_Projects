import sqlite3

connection = sqlite3.connect('library.db')

cursor = connection.cursor()

def existence_verification(title,author,released_year):
    cursor.execute("SELECT * FROM books where title = ? and author = ? and released_year = ?",(title, author, released_year,))
    finding_one = cursor.fetchall()
    if len(finding_one) == 1:
        #The book is already in the library
        return True
    else:
        return False

class Book:

    @staticmethod
    def add_to_the_library(title,author,released_year):
        if existence_verification(title,author,released_year):
            cursor.execute("UPDATE books SET quantity = quantity + 1 where title = ? and author = ? and released_year = ?", (title, author, released_year,))
            connection.commit()
            print("The book is already referenced, it's quantity has been modified")
        else:
            cursor.execute("INSERT INTO books(title,author,released_year)VALUES (?,?,?)", (title,author,released_year,))
            connection.commit()
            print("Book added")

    @staticmethod
    def remove_from_library(book_id):
        if Book.search_by_id(book_id):
            cursor.execute("DELETE FROM books WHERE book_id = ? ", (book_id,))
            connection.commit()

    @staticmethod
    def update(book_id):
        if Book.search_by_id(book_id):
            choice = input("Which of these caractetistics you want to modify title/author/year/quantity : ")

            if choice == "title":
                modification = input("New title : ")
                cursor.execute("UPDATE books SET title = ? WHERE  book_id = ? ", (modification, book_id,))
                connection.commit()
            if choice == "author":
                modification = input("New author : ")
                cursor.execute("UPDATE books SET author = ? WHERE  book_id = ? ", (modification, book_id,))
                connection.commit()
            if choice == "year":
                modification = int(input("New released year : "))
                cursor.execute("UPDATE books SET released_year = ? WHERE  book_id = ? ", (modification, book_id,))
                connection.commit()
            if choice == "quantity":
                modification = int(input("New quantity : "))
                cursor.execute("UPDATE books SET quantity = ? WHERE  book_id = ? ", (modification, book_id,))
                connection.commit()

    @staticmethod
    def search_by_id(book_id):
        cursor.execute("SELECT title, author, released_year FROM books where book_id = ? ", (book_id,))
        search = cursor.fetchone()

        if search is not None:
            print(f"The book {book_id} was found,this book is {search[0]} it was written by {search[1]} in {search[2]}")
            return True
        else:
            print(f"The book {book_id} was not found")
            return False

    @staticmethod
    def print_books():

        cursor.execute("SELECT * FROM books")
        every_books = cursor.fetchall()

        for book in every_books:
            print(f"{book[0]} : {book[1]} : {book[2]} : {book[3]} : {book[4]}")

    @staticmethod
    def search_by_keyword():
        key = input("Entrez votre requête : ")
        key_word = f"%{key}%"

        cursor.execute("SELECT title, author, released_year FROM books where title like ? OR author like ? OR released_year like ?",(key_word, key_word, key_word,))

        result = cursor.fetchall()
        for book in result:
            print(f"{book[0]} : {book[1]} : {book[2]} ")



Book.print_books()